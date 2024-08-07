# RAG-Mastery: A Personal Path from Basic to Master in RAG
Welcome to **RAG-Mastery**, my personal guide to mastering Retrieval-Augmented Generation (RAG). This repository is my space to document my journey from foundational concepts to the most advanced techniques, helping me understand and apply these methods effectively.

## Table of Contents

- [Introduction](#introduction)
- [Understanding RAG](#understanding-rag)
  - [Concepts](#concepts)
  - [Math](#math)
- [Techniques](#techniques)
  - [Basic Retrieval](#basic-retrieval)
  - [Using a Vector Database](#using-a-vector-database)
  - [Document Search](#document-search)
  - [Chat Assistant](#chat-assistant)
  - [Conversational Assistant](#conversational-assistant)
  - [Self-Corrective RAG](#self-corrective-rag)
  - [Query RAG](#query-rag)
  - [GraphRAG](#graphrag)
  - [RAG-Query on Python](#rag-query-on-python)
- [References](#references)

## Introduction
Retrieval-Augmented Generation (RAG) is a powerful framework that integrates retrieval into the sequence generation process. This framework combines the strengths of information retrieval and generative language models to enhance text generation capabilities. This approach operates by dynamically fetching relevant documents or data snippets based on a given query and using this retrieved information to generate a coherent and contextually appropriate response.

## Techniques
- **Simple RAG**  
  What I understand as a simple RAG is the use of indexing, retrieving information from documents, and generating an answer. This process is illustrated in the following diagram, which shows the key components and processes of RAG.
  
  ![Diagram Indexing, Retrieval, and Generation](https://github.com/Maucalderondelab/RAG-Mastery/blob/main/Diagrams/indexing_retrieval_generation.png)
  
  - **What have I learned?**  
    I used [LangChain](https://python.langchain.com/v0.2/docs/tutorials/), a popular framework for the use of LLMs. I learned the basics, such as how to use unstructured files, apply a split of the document, and embed the split documents. The most important part is defining a chain for the system, which consists of a template prompt that the system uses when a query or question is given. With the context (retrieved information), it tries to provide an answer.
  

## References
- [freedocecamp](https://www.freecodecamp.org/news/mastering-rag-from-scratch/)
- [HuggingFaces](https://search.brave.com/search?q=huggingfaces+RAG&source=desktop)
- [Paper](https://arxiv.org/abs/2005.11401)
