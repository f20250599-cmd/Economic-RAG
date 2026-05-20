# EcoSphere Intelligence: RAG Driven Framework
EcoSphere Intelligence: RAG-Driven Framework
Organized by: ACM-W
This repository contains the production-ready implementation used in the ACM-W workshop “Build Your First AI Chatbot: RAG with NVIDIA”.
EcoSphere Intelligence is an advanced Retrieval-Augmented Generation (RAG) framework engineered to architect precision retrieval and eliminate hallucinations across complex, fragmented data ecosystems. It bridges the gap between static LLM knowledge weights and dynamic enterprise data pipelines.

#Basics of RAG (Retrieval-Augmented Generation)

RAG is an architectural pattern that synchronizes semantic document retrieval with autoregressive text generation.
Rather than relying solely on parametric memory (pre-trained data), a RAG system orchestration pipeline:
Dynamically queries and retrieves top-$k$ relevant context blocks from ingested local documents based on semantic vector similarity.
Injects these blocks into the LLM prompt payload to anchor responses in source-of-truth verification.

This system architecture ensures:

Grounded Responses: Maximized empirical accuracy by constraining the LLM generation space.
Mitigated Hallucinations: Verifiable outputs tied directly to source documentation.
Data Privacy & Agility: Direct processing of private PDFs and runtime knowledge updates without expensive model fine-tuning.

#Technical Features & System Capabilities

Multi-Format Ingestion Engine: Concurrent, asynchronous processing of unstructured text (TXT) and structured binaries (PDF) via a unified UI entry point.
Granular Token Optimization: Automated document segmentation utilizing a custom chunk_text function set at a strict threshold of 150 tokens to preserve semantic density and eliminate context-window dilution.
Vector Embeddings Pipeline: High-dimensional semantic vector generation powered by NVIDIA NIM microservices endpoints.
Embedded Vector Database Storage: Local, high-performance indexing and storage management using ChromaDB to enable rapid spatial lookups.
Stateful Session Management: Native Streamlit session state architecture to maintain user and assistant message histories, ensuring coherent, multi-turn conversational memory.
Tech Stack
Core Runtime: Python
UI Architecture: Streamlit
Vector Storage Engine: ChromaDB
Inference & Embeddings: NVIDIA NIM API
Parsing Utilities: PyPDF2 & Requests
Environment Management: python-dotenv
How to Run the Project
Clone the github repository



Bash
git clone <PASTE YOUR GITHUB REPO LINK HERE>


Go inside the project folder



Bash
cd <YOUR REPO FOLDER NAME>


Install all required python packages



Bash
pip install streamlit requests chromadb PyPDF2 python-dotenv


Create a file to store your nvidia api key (.env) & add your nvidia api key to the .env file



Bash
NVIDIA_API_KEY=nvapi-xxxxxxxxxxxxxxxx


Run the streamlit application ```bash
streamlit run main.py



---

## Evaluator Notes:
  - **Local Persistence**: The vector database indices are initialized and cached locally on your machine, eliminating external cloud data dependencies.
  - **Cross-Document Synthesis**: The framework executes global queries, allowing the retrieval mechanism to synthesize information simultaneously across multiple separate source documents.
  - **Index Cache Invalidation**: To reset the knowledge base or clear out memory leaks, simply delete the local Chroma storage folder to re-initialize the indexing pipeline.


