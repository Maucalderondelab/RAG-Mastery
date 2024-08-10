import sys
import os
from typing import List


# Import your SimpleRAG class and API_KEY
from helper_function import SimpleRAG, API_KEY
from langchain.schema.document import Document
from langchain.schema.retriever import BaseRetriever
from langchain_mistralai.chat_models import ChatMistralAI

import warnings
# Suppress the specific warning
warnings.filterwarnings("ignore", message="Could not download mistral tokenizer")
import logging
logging.getLogger().setLevel(logging.WARNING)
# Suppress HTTP request logs
logging.getLogger("httpx").setLevel(logging.WARNING)

# Suppress FAISS logs
logging.getLogger("faiss").setLevel(logging.WARNING)

# Suppress pikepdf logs
logging.getLogger("pikepdf").setLevel(logging.WARNING)

def main() -> None:
    folder_path: str = "/home/mauricio/Documents/Projects/RAG-Mastery/data"
    
    # Initialize the SimpleRAG
    rag: SimpleRAG = SimpleRAG(API_KEY)  # Initialize with None for retriever initially
    # Use the instance methods
    documents: List[Document] = rag.load_documents(folder_path)
    splits: List[Document] = rag.split_documents(documents)
    retriever: BaseRetriever = rag.embed_documents(splits)

    # Update the retriever in the rag instance
    rag.retriever = retriever

    # Initialize the LLM    
    rag.llm: ChatMistralAI = rag.get_llm_model()

    print("\nWelcome to the NFL 🏈 Rule Assistant!")
    print("Ask questions about NFL rulebook of 2024, or type 'quit' to exit.")

    while True:
        user_input: str = input("\n 🔍Your question: ")
        
        if user_input.lower() == 'quit' or user_input.lower() == 'exit':
            print("Thank you for using the NFL 🏈 Rule Assistant 2024. Goodbye!")
            break

        try:
            response = rag.rag_chain(user_input)
            print("\n 🤖 Assistant:", response.content)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
