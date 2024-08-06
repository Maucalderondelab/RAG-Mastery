import sys
import os
from typing import List, Union

from langchain_mistralai.chat_models import ChatMistralAI
from langchain_unstructured import UnstructuredLoader
from langchain.schema.document import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import ChatPromptTemplate
from langchain.schema import AIMessage
from langchain.schema.retriever import BaseRetriever


# Path to the directory containing config.py
config_path = '/home/mauricio/Documents/Projects/RAG-Mastery'

# Add the directory to sys.path
if config_path not in sys.path:
    sys.path.append(config_path)

# Now you can import the API_KEY from config.py
from config import API_KEY
# Define path_to_docs here since it's no longer in the class


    
class SimpleRAG:
    def __init__(self, api_key: str):
        self.API_KEY: str = api_key
        self.prompt_template : ChatPromptTemplate= ChatPromptTemplate.from_messages([
            ("system", "You are an rule assistant for the NFL. Answer the questions based on the context provided. If the answer to the question is not in the context, say \"I don't know\"."),
            ("human", "Context: {context}\n\nQuestion: {question}\nAnswer:")
        ])
        self.folder_path: str = "/home/mauricio/Documents/Projects/RAG-Mastery/docs"
        self.llm_model : ChatMistralAI = self.get_llm_model()
        self.retriever : BaseRetriever 

    def get_llm_model(self)-> ChatMistralAI:
        return ChatMistralAI(
            model_name="open-mixtral-8x22b", 
            mistral_api_key=self.API_KEY
        )


    def load_documents(self, folder_path: str) -> List[Document]:
        documents = []
        for file in os.listdir(folder_path):
            if file.endswith('.docx') or file.endswith('.pdf') or file.endswith('.txt'):
                loader = UnstructuredLoader(os.path.join(folder_path, file))
                documents.extend(loader.load())
            
        print("✅ Documents loaded successfully")
        print("     Document loaded lenght: ", len(documents))
        print("     File name: ", documents[0].metadata.get("filename"))
        return documents


    def split_documents(self, documents: List[Document], chunk_size: int = 1000, chunk_overlap: int = 200) -> List[Document]:
            try:
                text_splitter: RecursiveCharacterTextSplitter = RecursiveCharacterTextSplitter(
                    chunk_size=chunk_size,
                    chunk_overlap=chunk_overlap,
                    length_function=len,
                    separators=["\n\n", "\n", " ", ""]
                )
                splits: List[Document] = text_splitter.split_documents(documents)
                print("✅ Split document successfully")
                print("     Documents split: ", len(splits))
                return splits
            except Exception as e:
                print(f"Error splitting documents: {e}")
                raise
            

    def embed_documents(self, splits: List[Document]) -> BaseRetriever:
        try:
            embeddings: MistralAIEmbeddings = MistralAIEmbeddings(
                model="mistral-embed",
                mistral_api_key=self.API_KEY
            )
            vectorstore: FAISS = FAISS.from_documents(documents=splits, embedding=embeddings)
            retriever: BaseRetriever = vectorstore.as_retriever(
                search_type="mmr",
                search_kwargs={"k": 6},
            )

            print("✅ Retriever successfully created")
            return retriever
        except Exception as e:
            print(f"Error embedding/retrieving documents {e}")
            raise

    def rag_chain(self, question: str) -> AIMessage:
        context: List[Document] = self.retriever.invoke(question)
        context_str: str = "\n".join([doc.page_content for doc in context])
        
        messages = self.prompt_template.format_messages(
            context=context_str,
            question=question
        )
        
        response: AIMessage = self.llm.invoke(messages)
        
        return response
    