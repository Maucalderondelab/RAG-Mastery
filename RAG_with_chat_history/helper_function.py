import sys
import os
from typing import List, Union

from langchain_mistralai.chat_models import ChatMistralAI
from langchain_unstructured import UnstructuredLoader
from langchain.schema.document import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_history_aware_retriever
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_unstructured import UnstructuredLoader
from langchain.schema.document import Document
from langchain.schema import BaseRetriever


# Path to the directory containing config.py
config_path = '/home/mauricio/Documents/Projects/RAG-Mastery'

# Add the directory to sys.path
if config_path not in sys.path:
    sys.path.append(config_path)

# Now you can import the API_KEY from config.py
from config import API_KEY
# Define path_to_docs here since it's no longer in the class

class Chat_history_RAG():
    def __init__(self, docx_file_path, mistral_key=API_KEY):
        self.DOCX_FILE_PATH = docx_file_path
        self.mistral_key = mistral_key

    def get_llm_model(self)-> ChatMistralAI:
        return ChatMistralAI(
            model_name="open-mixtral-8x22b", 
            mistral_api_key=self.mistral_key
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
            

    def embed_documents(self, splits: List[Document]):
        try:
            embeddings: MistralAIEmbeddings = MistralAIEmbeddings(
                model="mistral-embed",
                mistral_api_key=self.mistral_key
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
    def create_history_chain(self, retriever: BaseRetriever):
        llm_model = self.get_llm_model()
        contextualize_q_system_prompt = """
            You are an AI assistant specializing in contextual analysis and question reformulation for an NFL rulebook system. Your task is to:

            1. Carefully analyze the provided chat history and the latest user question.
            2. Identify any contextual references or implied information from the chat history that are relevant to the latest question.
            3. Reformulate the question into a standalone format that incorporates all necessary context.
            4. Ensure the reformulated question can be fully understood without access to the chat history.
            5. If the original question is already standalone and doesn't require additional context, return it unchanged.

            Key Instructions:
            - Focus solely on reformulation; do not attempt to answer the question.
            - Maintain the original intent and scope of the question.
            - Use clear, concise language appropriate for an NFL rulebook context.
            - Include specific NFL terminology or references if they were part of the original context.

            Example:
            Original: "What's the penalty for that?"
            Reformulated: "What is the specific penalty for defensive pass interference in the NFL?"

            Output: Provide only the reformulated question or the original question if no reformulation is needed. Do not include any explanations or additional commentary.
            """
        

        contextualize_q_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", contextualize_q_system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
            )
        system_prompt = (
            """
                You are an expert NFL rulebook assistant specializing in concise, accurate answers. 
                Your primary function is to provide clear and precise responses to questions about NFL rules and regulations. 
                Key Instructions:
                    1. Analyze the provided context carefully.
                    2. Use only the given context to formulate your answer. Do not rely on external knowledge.
                    3. If the context doesn't contain sufficient information to answer the question, respond with 'I don't have enough information to answer that question based on the provided context.
                    4. Limit your response to a maximum of three sentences.
                    5. Prioritize clarity and accuracy over exhaustive explanations.
                    6. If relevant, cite the specific NFL rule or section number.
                    7. Avoid speculation or personal opinions.
                    
                Context:
                {context}
            """
        )

        qa_prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ])

        history_aware_retriever = create_history_aware_retriever(
            llm_model, retriever, contextualize_q_prompt)

        question_answer_chain = create_stuff_documents_chain(llm_model, qa_prompt)

        rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
    
        return rag_chain

    def rag_chain(self):
        
        documents = self.load_documents(folder_path=self.DOCX_FILE_PATH)
        splits = self.split_documents(documents)
        retriever = self.embed_documents(splits)
        rag_chain = self.create_history_chain(retriever)
        
        store = {}

        def get_session_history(session_id: str) -> BaseChatMessageHistory:
            if session_id not in store:
                store[session_id] = ChatMessageHistory()
            return store[session_id]
    
        chain = RunnableWithMessageHistory(
            rag_chain,
            get_session_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer",
        )

        print("✅ Self-corrective chain created successfully ")
        return chain