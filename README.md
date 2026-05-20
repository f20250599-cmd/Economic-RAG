# EcoSphere Intelligence: RAG Driven Framework

EcoSphere Intelligence is an advanced Retrieval-Augmented Generation (RAG) framework engineered to architect precision retrieval and eliminate hallucinations across complex, fragmented data ecosystems. 

It bridges the gap between static LLM knowledge weights and dynamic enterprise data pipelines.


## Basics of RAG (Retrieval-Augmented Generation)

RAG is a technique that combines *document retrieval* with *text generation*.

Instead of answering only from what a model already knows, a RAG system:
- First searches relevant information from uploaded documents  
- Then uses that information as context to generate accurate answers  

This makes the chatbot:
- More accurate  
- Less likely to hallucinate  
- Able to answer from private PDFs and documents  
- Easy to update without retraining the model

## Problem Statement

Traditional financial and economic reports are often:

● lengthy
● difficult to analyze quickly
● filled with technical data
● time consuming to interpret manually
Users may struggle to:

● identify important economic insights
● understand inflation trends
● analyze market sentiment
● extract key information from large reports.

## Project Goal

To build an AI-powered Economic News Intelligence System using RAG (Retrieval Augmented
Generation) that can:
* ✔analyze uploaded economic reports and financial news
* ✔retrieve relevant information from documents
* ✔generate summarized economic insights
* ✔ identify inflation trends and sentiment
* ✔ provide contextual answers to user queries in natural language

## Tech Stack

* Core Runtime: Python
* UI Architecture: Streamlit
* Vector Storage Engine: ChromaDB
* LLM & Embeddings: NVIDIA NIM API
* Parsing Utilities: PyPDF2 & Requests
* Environment Management: python-dotenv

## How to Run the Project

Clone the github repository
bash
git clone <PASTE YOUR GITHUB REPO LINK HERE>


Go inside the project folder
bash
cd <YOUR REPO FOLDER NAME>


Install all required python packages
bash
pip install streamlit requests chromadb PyPDF2 python-dotenv


Create a file to store your nvidia api key (.env) & add your nvidia api key to the .env file
bash
NVIDIA_API_KEY=nvapi-xxxxxxxxxxxxxxxx


Run the streamlit application 
bash
streamlit run main.py



## Important Notes:
  - The vector database is created locally on your system
  - You can upload multiple files and the chatbot will answer using all of them
  - To reset everything, delete the chroma folder or use the clear option if available



