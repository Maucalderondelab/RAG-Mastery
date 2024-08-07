# RAG-Mastery: A Personal Path from Basic to Master in RAG
Welcome to **RAG-Mastery**, my personal guide to mastering Retrieval-Augmented Generation (RAG). This repository is my space to document my journey from foundational concepts to the most advanced techniques, helping me understand and apply these methods effectively.

## Table of Contents

- [Introduction](#introduction)
- [Understanding RAG](#understanding-rag)
  - [Concepts](#concepts)
  - [Math](#math)
- [Techniques](#techniques)
  - [Simple RAG](#basic-retrieval)
  - [RAG with chat history](#conversational-assistant)
  - [RAG with a Vector Database](#using-a-vector-database)
  - [RAG-Query on Python](#rag-query-on-python)
  - [Self-Corrective RAG](#self-corrective-rag)
  - [Agents](#query-rag)
  - [GraphRAG](#graphrag)
  
- [References](#references)

## Introduction
Retrieval-Augmented Generation (RAG) is a powerful framework that integrates retrieval into the sequence generation process. This framework combines the strengths of information retrieval and generative language models to enhance text generation capabilities. This approach operates by dynamically fetching relevant documents or data snippets based on a given query and using this retrieved information to generate a coherent and contextually appropriate response.

## Techniques

### 1) Simple RAG
**Simple RAG** involves indexing, retrieving information from documents, and generating an answer. This process is illustrated in the diagram below:

![Diagram Indexing, Retrieval, and Generation](https://github.com/Maucalderondelab/RAG-Mastery/blob/main/Diagrams/indexing_retrieval_generation.png)

**What have I learned?**

I used [LangChain](https://python.langchain.com/v0.2/docs/tutorials/), a popular framework for the use of LLMs. I learned the basics, such as:
- Using unstructured files
- Splitting documents
- Embedding split documents
- Defining a chain for the system

The chain consists of a template prompt that the system uses when a query or question is given. With the context (retrieved information), it tries to provide an answer.

  

## References
- [freedocecamp](https://www.freecodecamp.org/news/mastering-rag-from-scratch/)
- [HuggingFaces](https://search.brave.com/search?q=huggingfaces+RAG&source=desktop)
- [Paper](https://arxiv.org/abs/2005.11401)
