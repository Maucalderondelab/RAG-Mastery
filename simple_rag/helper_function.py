import sys
import os
import tqdm as notebook_tqdm
from typing import List, Union

from langchain_mistralai.chat_models import ChatMistralAI
from langchain_unstructured import UnstructuredLoader
from langchain.schema.document import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import ChatPromptTemplate


# Path to the directory containing config.py
config_path = '/home/mauricio/Documents/Projects/RAG-Mastery'

# Add the directory to sys.path
if config_path not in sys.path:
    sys.path.append(config_path)

# Now you can import the API_KEY from config.py
from config import API_KEY
# Define path_to_docs here since it's no longer in the class


    
class SimpleRAG:
    def __init__(self, api_key):
        self.API_KEY = api_key
        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", "You are an rule assistant for the NFL. Answer the questions based on the context provided. If the answer to the question is not in the context, say \"I don't know\"."),
            ("human", "Context: {context}\n\nQuestion: {question}\nAnswer:")
        ])

    def get_llm_model(self):
        return ChatMistralAI(
            model_name="open-mixtral-8x22b", 
            mistral_api_key=self.API_KEY
        )


    def load_documents(self, folder_path):
        documents = []
        for file in os.listdir(folder_path):
            if file.endswith('.docx') or file.endswith('.pdf') or file.endswith('.txt'):
                loader = UnstructuredLoader(os.path.join(folder_path, file))
                documents.extend(loader.load())
            print("Document loaded lenght: ", len(documents))
        print("Documents loaded successfully ✅")
        print(documents[0].metadata.get("filename"))
        return 


    def split_documents(self, documents, chunk_size= 1000, chunk_overlap= 200):
            try:
                text_splitter: RecursiveCharacterTextSplitter = RecursiveCharacterTextSplitter(
                    chunk_size=chunk_size,
                    chunk_overlap=chunk_overlap,
                    length_function=len,
                    separators=["\n\n", "\n", " ", ""]
                )
                splits: List[Document] = text_splitter.split_documents(documents)
                print("Split document successfully ✅")
                print("Documents split: ", len(splits))
                return splits
            except Exception as e:
                print(f"Error splitting documents: {e}")
                raise
            

    def embed_documents(self, splits):
        try:
            embeddings = MistralAIEmbeddings(
                model="mistral-embed",
                mistral_api_key=API_KEY
                )
            vectorstore = FAISS.from_documents(documents=splits, embedding=embeddings)
            retriever = vectorstore.as_retriever(
                search_type="mmr",
                search_kwargs={"k": 6},
            )

            print("Retriever succesfuly created ✅")
            return retriever
        except Exception as e:
            print(f"Error embeding/retrieving documents {e}")
            raise

    def rag_chain(self, question):

        
        # Format the messages
        # Retrieve the relevant documents
        context = self.retriever.get_relevant_documents(question)
        context_str = "\n".join([doc.page_content for doc in context])
        
        # Format the messages
        messages = self.prompt_template.format_messages(
            context=context_str,
            question=question
        )
        
        # Generate the answer
        response = self.llm.invoke(messages)
        
        return response