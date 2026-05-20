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


## Technical Features & System Capabilities

* Multi-format document ingestion (TXT & PDF)
* Semantic chunking pipeline with optimized token segmentation
* NVIDIA-powered embedding generation
* ChromaDB vector storage for fast similarity search
* Context-aware response generation
* Stateful Streamlit chat session management
* Multi-turn conversational memory
* Local vector database persistence
* Retrieval-first response architecture


## System Workflow

1. Upload documents (TXT/PDF)
2. Extract and split document text into chunks
3. Generate embeddings using NVIDIA NIM APIs
4. Store embeddings inside ChromaDB
5. Perform semantic similarity search for user queries
6. Retrieve top-k relevant chunks
7. Send retrieved context to the LLM
8. Generate grounded AI responses


## Tech Stack

Component	Technology
Core Runtime	Python
UI Framework	Streamlit
Vector Database	ChromaDB
Embeddings & Inference	NVIDIA NIM API
PDF Parsing	PyPDF2
HTTP Requests	Requests
Environment Handling	python-dotenv


## How to Run the Project

*Clone the github repository*
bash
git clone <PASTE YOUR GITHUB REPO LINK HERE>


*Go inside the project folder*
bash
cd <YOUR REPO FOLDER NAME>


*Install all required python packages*
bash
pip install streamlit requests chromadb PyPDF2 python-dotenv


*Create a file to store your nvidia api key (.env) & add your nvidia api key to the .env file*
bash
NVIDIA_API_KEY=nvapi-xxxxxxxxxxxxxxxx



*Run the streamlit application* 
bash
streamlit run main.py


## Important Notes:
  - The vector database is created locally on your system
  - You can upload multiple files and the chatbot will answer using all of them
  - To reset everything, delete the chroma folder or use the clear option if available



