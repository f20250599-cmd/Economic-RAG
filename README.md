# EcoSphere Intelligence: RAG Driven Framework

Organized by ACM-W

EcoSphere Intelligence is an advanced Retrieval-Augmented Generation (RAG) framework designed to deliver precise, grounded, and context-aware AI responses using enterprise and local document knowledge bases.

It bridges the gap between static LLM knowledge and dynamic real-world data pipelines by combining semantic retrieval with autoregressive text generation.

⸻

Basics of RAG (Retrieval-Augmented Generation)

RAG is an AI architecture that combines:

* Semantic document retrieval
* Large Language Model (LLM) text generation

Instead of relying only on pre-trained model memory, the system:

* Searches the most relevant information from uploaded documents
* Retrieves semantically similar context chunks
* Injects retrieved context into the LLM prompt
* Generates grounded and verifiable responses

This approach enables:

* Higher factual accuracy
* Reduced hallucinations
* Real-time knowledge updates
* Secure querying of private documents
* No expensive model retraining

⸻

Technical Features & System Capabilities

* Multi-format document ingestion (TXT & PDF)
* Semantic chunking pipeline with optimized token segmentation
* NVIDIA-powered embedding generation
* ChromaDB vector storage for fast similarity search
* Context-aware response generation
* Stateful Streamlit chat session management
* Multi-turn conversational memory
* Local vector database persistence
* Retrieval-first response architecture

⸻

System Workflow

1. Upload documents (TXT/PDF)
2. Extract and split document text into chunks
3. Generate embeddings using NVIDIA NIM APIs
4. Store embeddings inside ChromaDB
5. Perform semantic similarity search for user queries
6. Retrieve top-k relevant chunks
7. Send retrieved context to the LLM
8. Generate grounded AI responses

⸻

Tech Stack

Component	Technology
Core Runtime	Python
UI Framework	Streamlit
Vector Database	ChromaDB
Embeddings & Inference	NVIDIA NIM API
PDF Parsing	PyPDF2
HTTP Requests	Requests
Environment Handling	python-dotenv

⸻

How to Run the Project

Clone the Repository

git clone <YOUR_GITHUB_REPOSITORY_LINK>

⸻

Navigate to the Project Directory

cd <YOUR_PROJECT_FOLDER_NAME>

⸻

Install Required Dependencies

pip install streamlit requests chromadb PyPDF2 python-dotenv

⸻

Configure NVIDIA API Key

Create a .env file inside the project directory and add:

NVIDIA_API_KEY=nvapi-xxxxxxxxxxxxxxxx

⸻

Run the Streamlit Application

streamlit run main.py

⸻

Important Notes

* Vector embeddings are stored locally on the system
* Multiple document uploads are supported
* The chatbot retrieves answers from all uploaded files
* To reset the vector database, delete the chroma/ folder
* Session history is maintained during runtime

⸻

Future Enhancements

* Hybrid search (semantic + keyword retrieval)
* GPU-accelerated local inference
* Role-based authentication
* Persistent cloud vector storage
* Multi-model LLM routing
* Advanced reranking pipelines
* Real-time document synchronization

⸻

Project Objective

EcoSphere Intelligence demonstrates how modern RAG pipelines can be used to create reliable, scalable, and enterprise-ready AI assistants capable of interacting with private knowledge ecosystems efficiently and securely.
