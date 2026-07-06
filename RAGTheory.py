###3 Phases of RAG ###
"""
Phase 1: INGESTION (done once ,offline)
- Load your Documents,
- split them into chunks (ex 500charecters),
- create embeddings for each chunk (list of numbers that represent the chunk)
- Store the embeddings in a vector database (ex: FAISS, Weaviate, Pinecone, etc)


Phase 2: RETRIEVAL
 - convert the user question into an embedding
 - search the vector database for the most similar chunks to the user question embedding
 - return top3-5 most match relevent chunks

Phase 3: GENERATION
 - Build the prompt for the LLM using the user question 
 - Send to LLM 
 - LLM will retreive context and generate answer 
 - return answer to the user


What is Embedding?
An embedding is a numerical representation of data, often in the form of a vector.

what is a vector database?



"""