# rag_chain.py
from embed_client import get_embeddings
from vector_store import query_vectorstore


def build_prompt(query: str) -> str:
    """
    Build the final prompt we send to the LLM.

    Steps:
    1. Embed the user's question
    2. Retrieve similar document chunks from ChromaDB
    3. Combine context + question into a single prompt string
    """
    # 1) Embed the query
    query_embedding = get_embeddings([query])[0]

    # 2) Get top-k similar chunks
    retrieved_docs = query_vectorstore(query_embedding)

    # 3) Join them into a context section
    context = "\n".join(retrieved_docs)

    # 4) Build the prompt
    prompt = (
        "You are an Economic News Intelligence Assistant.\n"
    "Use the financial news context below to answer the question.\n\n"
    "Your answer should include:\n"
    "1. Short Summary\n"
    "2. Sentiment: Positive, Negative, or Neutral\n"
    "3. Key Economic Insights\n"
    "4. Affected sectors or companies if mentioned\n"
    "5. Possible market or economic impact\n\n"
    "If the context does not contain enough information, say so clearly.\n\n"
    "Do not mention companies, sectors, or facts that are not explicitly present in the provided context.\n\n"
    "If the user greets casually or asks normal conversational questions, respond naturally without relying heavily on the document context.\n\n"
    f"Context:\n{context}\n\n"
    f"Question:\n{query}"
    )

    return prompt

