import sys
import os
from typing import List


# Import your SimpleRAG class and API_KEY
from helper_function import Chat_history_RAG, API_KEY
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
    RAG_chat_history: Chat_history_RAG = Chat_history_RAG(folder_path)
    chain = RAG_chat_history.rag_chain()

    print("\nWelcome to the NFL 🏈 Rule Assistant!")
    print("Ask questions about NFL rulebook of 2024, or type 'quit' to exit.")

    while True:
        user_input: str = input("\n 🔍Your question: ")
        
        if user_input.lower() == 'quit' or user_input.lower() == 'exit':
            print("Thank you for using the NFL 🏈 Rule Assistant 2024. Goodbye!")
            break

        try:
            result = chain.invoke(
                {"input": "How do these new kickoff rules affect onside kick attempts?"},
                config={
                    "configurable": {"session_id": "nfl_rules_2024"}
                },
                )
           
            print("\n 🤖 Assistant:", result['input'])
            print(f"🔵 Chat History: {result['chat_history']}")
            print(f"🟠 Answer: {result['answer']}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
