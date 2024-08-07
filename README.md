# RAG-Mastery a personal path from basic to master in RAG
Welcome to **RAG-Mastery**, my personal guide to mastering Retrieval-Augmented Generation (RAG). This repository is my space to document my journey from foundational concepts through to the most advanced techniques, helping me understand and apply these methods effectively.

## Table of Contents

- [Introduction to RAG](#introduction-to-rag)
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
Retrieval-Augmented Generation (RAG) is a powerful framework that integrates retrieval into the sequience generation process. This framework combines the strengths of information retrieval and generative lenaguage models to enchance text generation capabilities. This approach operates by dynaically fetching relevant documents or data snippetss based on a given query and using this retrieved information to generate a coherent and contextually appropiate response.

## Techniques
- Simple RAG
  What I understand as a simple RAG is the use of indexin, retrieval the infomtion of the documents and genetare an answer. I have this ilustrated in this diagram. A simple diagram that show te key components and procces of RAG is this one.
![Diagram Indexin, retrieval and generation](https://github.com/Maucalderondelab/RAG-Mastery/blob/main/Diagrams/indexing_retrieval_generation.png)
    - What have i learned?
      
      I used [langchain](https://python.langchain.com/v0.2/docs/tutorials/) very popular framework for the use of LLMs. I learned the basic like how to call use unstruted files calling hten apply a split of the document. How to apply embeddings into the splitted document and the most importat part define a chain for the system, the chain consist in a template prompt that the system uses when a query or question is given, then with the context (retrieved information) it tries to give you an aswer  

## References
- [freedocecamp](https://www.freecodecamp.org/news/mastering-rag-from-scratch/)
- [HuggingFaces](https://search.brave.com/search?q=huggingfaces+RAG&source=desktop)
- [Paper](https://arxiv.org/abs/2005.11401)
