import sys
import os

# Import your SimpleRAG class and API_KEY
from helper_function import SimpleRAG, API_KEY



def main():
    folder_path = "/home/mauricio/Documents/Projects/RAG-Mastery/data"
    
    # Initialize the SimpleRAG
    rag = SimpleRAG(API_KEY)  # Initialize with None for retriever initially

    # Use the instance methods
    documents = rag.load_documents(folder_path)
    splits = rag.split_documents(documents)
    retriever = rag.embed_documents(splits)

    # Update the retriever in the rag instance
    rag.retriever = retriever

    # Initialize the LLM
    rag.llm = rag.get_llm_model()

    print("Welcome to the NFL Rule Assistant!")
    print("Ask questions about NFL rules, or type 'quit' to exit.")

    while True:
        user_input = input("\nYour question: ")
        
        if user_input.lower() == 'quit':
            print("Thank you for using the NFL Rule Assistant. Goodbye!")
            break

        try:
            response = rag.rag_chain(user_input)
            print("\nAssistant:", response.content)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()