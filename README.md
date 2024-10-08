# RAG-Mastery: A Personal Path from Basic to Master in RAG

Welcome to **RAG-Mastery**, my personal guide to mastering Retrieval-Augmented Generation (RAG). This repository is my space to document my journey from foundational concepts to the most advanced techniques, helping me understand and apply these methods effectively.

# Table of Contents
- [Introduction](#introduction)
- [Basic RAG](#basic-rag)
  - [RAG](#rag)
  - [RAG with chat history](#rag-with-chat-history)
  - [Retrieval with a Vector Database](#retrieval-with-a-vector-database)
  - [LLM executing Python code](#llm-executing-python-code)
- [Advanced RAG](#advanced-rag)
  - [Self-Reflective RAG](#self-reflective-rag)
  - [Multi-step Retrieval](#multi-step-retrieval)
  - [Hybrid Search](#hybrid-search)
  - [Query Enhancement](#query-enhancement)
  - [Adaptive Retrieval](#adaptive-retrieval)
- [Agents](#agents)
- [References](#references)

# Introduction

Retrieval-Augmented Generation (RAG) is a powerful framework that integrates retrieval into the sequence generation process. This framework combines the strengths of information retrieval and generative language models to enhance text generation capabilities. This approach operates by dynamically fetching relevant documents or data snippets based on a given query and using this retrieved information to generate a coherent and contextually appropriate response.

# Basic RAG

## RAG

**RAG or Simple RAG** involves indexing, retrieving information from documents, and generating an answer. This process is illustrated in the diagram below:

![Diagram Indexing, Retrieval, and Generation](https://github.com/Maucalderondelab/RAG-Mastery/blob/main/Diagrams/indexing_retrieval_generation.png)
*Simple RAG Implementation*

In the `simple_rag` folder, you will find three notebooks that demonstrate different aspects of implementing a Simple RAG:

1. [Detailed Explanation Notebook](https://github.com/Maucalderondelab/RAG-Mastery/blob/main/simple_rag/simple_rag.ipynb)
    - This Jupyter Notebook provides a detailed explanation of the functions used or built throughout the project.

2. [Chat Assistant in Terminal](https://github.com/Maucalderondelab/RAG-Mastery/blob/main/simple_rag/main.py) and 3 [Helper Functions](https://github.com/Maucalderondelab/RAG-Mastery/blob/main/simple_rag/helper_function.py)
    - The main file is designed to create a chat-like assistant that runs in the terminal. It has some prints with the information that and the model is retrieving.
   ![](https://github.com/Maucalderondelab/RAG-Mastery/blob/main/simple_rag/chat-terminal.png)
    - The helper_function file is the code from the detailed explanation into a single function for ease of use.

**What have I learned?**

I used [LangChain](https://python.langchain.com/v0.2/docs/tutorials/), a popular framework for the use of LLMs. I learned the basics, such as:
- Using unstructured files
- Splitting documents
- Embedding split documents
- Defining a chain for the system

The chain consists of a template prompt that the system uses when a query or question is given. With the context (retrieved information), it tries to provide an answer.

## RAG with chat history
We use the basics from our Simple_rag implementation, to be more specific we will be reusing:

- Document loading
- Text splitting
- Document retrieval

These components will remain largely unchanged, as they form the foundation of our RAG system. We're now focusing on enhancing our RAG system with an advanced chat history component, this involves creating a sub-chain that reformulates the user's latest question by incorporating context from the entire conversation history. 

$$
(query, conversation\hspace{0.1cm}history) --> LLM --> rephrased\hspace{0.1cm}query --> retriever
$$

This process allows us to maintain conversation fluently while ensuring that each query to the retriever is relevant information.



![Diagram Indexing, Retrieval, and Generation](https://github.com/Maucalderondelab/RAG-Mastery/blob/main/Diagrams/RAG-chat-history.png))
*Simple RAG Implementation*

In the `RAG wiht chat history` folder, you will find three notebooks that demonstrate different aspects of implementing a history context for our RAG:

1. [Detailed Explanation Notebook](https://github.com/Maucalderondelab/RAG-Mastery/blob/main/RAG_with_chat_history/RAG_history.ipynb)
    - This Jupyter Notebook provides a detailed explanation of the functions used or built throughout the project.

2. [Chat Assistant in Terminal](https://github.com/Maucalderondelab/RAG-Mastery/blob/main/RAG_with_chat_history/main.py) and 3 [Helper Functions](https://github.com/Maucalderondelab/RAG-Mastery/blob/main/RAG_with_chat_history/helper_function.py)
    - The main file is designed to create a chat-like assistant that runs in the terminal. It includes print statements that display the information the model is retrieving. Additionally, the chat history is printed after each question. On the first question, the chat history is empty, but as we continue to ask questions, the assistant stores the history and uses that information to provide better responses.
   ![](https://github.com/Maucalderondelab/RAG-Mastery/blob/main/RAG_with_chat_history/chat_terminal.png)
    - The helper_function file is the code from the detailed explanation into a single function for ease of use.

**What have I learned?**

I used [LangChain](https://python.langchain.com/v0.2/docs/tutorials/). I learned how to create a more complex RAG system:

* History aware: A module designed to retrieve information while considering the chat history, ensuring context-aware responses.

* Question answer: A structured chain that manages the flow of questions and answers, facilitating smooth and logical interactions.

* Chain: The core Retrieval-Augmented Generation chain, which combines retrieval with generation to produce highly relevant and accurate responses.
The chain consists of a template prompt that the system uses when a query or question is given. With the context (retrieved information), it tries to provide an answer.

## Retrieval with a Vector Database
This project explores 2 ways to perform searches in a SQL database using Language Models (LLMs). We're using a PostgreSQL database containing information about NFL teams.

![Diagram Indexing, Retrieval, and Generation](https://github.com/Maucalderondelab/RAG-Mastery/blob/main/Diagrams/RAG-chat-history.png)

We import the following classes from Langchain:
- `SQLDatabase`: For connecting and interacting with our database
- `SQLDatabaseChain`: Used to create a chain that generates SQL queries and interprets the results using our LLM

The workflow is:

1. Test the database connection to ensure it's running properly and can perform queries.
2. Create a more complex database chain, importing libraries for creating message templates.
3. Define key functions:
   - `retrieve_from_db`: Uses the `db_chain` to execute queries and extract results from the returned dictionary.
   - `generate`: Creates responses based on the following components:
     - A `system_message` that sets the role and behavior for the AI.
     - A template that structures the human's input, including placeholders for the actual query and the database context.
     - Calls the LLM to generate and return the response.



##  LLM executing Python code
![Diagram Indexing, Retrieval, and Generation](https://github.com/Maucalderondelab/RAG-Mastery/blob/main/Diagrams/llm_exec_python.png)

This project sets up a LangChain agent capable of executing Python code as part of its decision-making process.
  * We package the Python REPL functionality for use by the LangChain agent
  * We import the AgentFinish class from LangChain. This is typically used to represent the final output of an agent's execution.
  * We initialize the agent using the initialize_agent function, with the following parameters:
    * `tools=[python_tool]`: Provides the Python REPL tool to the agent.
    *  `llm=llm`: Assigns a predefined language model to the agent.
    * `agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION`: Specifies a zero-shot agent type.
    * `verbose=True`: Enables detailed logging of the agent's process.
    * `handle_parsing_errors=True`: Enables improved error handling.      

# Advanced RAG

## Self-Reflective RAG

[Content for Self-Reflective RAG]

## Multi-step Retrieval

[Content for Multi-step Retrieval]

## Hybrid Search

[Content for Hybrid Search]

## Query Enhancement

[Content for Query Enhancement]

## Adaptive Retrieval

[Content for Adaptive Retrieval]

# Agents

[Content for Agents]

# References

- [freedocecamp](https://www.freecodecamp.org/news/mastering-rag-from-scratch/)
- [HuggingFaces](https://search.brave.com/search?q=huggingfaces+RAG&source=desktop)
- [Paper](https://arxiv.org/abs/2005.11401)
