from matplotlib import text
from openai import OpenAI
from dotenv import load_dotenv
import os
import chromadb
load_dotenv()
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("OPENAI_API_KEY")
    )
chroma = chromadb.Client()
collection = chroma.get_or_create_collection("handbook")
def load_and_store(filepath):
    with open(filepath,'r',encoding='utf-8') as f:
        text = f.read()
    chunks = []
    current = []
    for line in text.split('\n\n'):
        line = line.strip()
        if not line or line.startswith('---') or line == '# Student Handbook — B.Tech Program':
            continue
        if line.startswith('## '):          # new section starts
            if current:
                chunks.append("\n".join(current))
            current = [line]
        else:
            current.append(line)
    if current:
        chunks.append("\n".join(current))        
    collection.add(
            documents=chunks,
            ids=[f"doc_{i}" for i in range(len(chunks))],
    )
def ask(question):
    results = collection.query(
        query_texts=[question],
        n_results=4
    )
    chunks = results['documents'][0]
    print(f"Retrieved chunks: {chunks}")
    context = "\n".join(chunks)
    ###Build prompt for LLM
    rag_prompt = f''' You are a helpful assistant answering questions about a college handbook.
Use ONLY the context below. You may apply a general rule to a specific case if it
reasonably fits. If the context genuinely contains nothing relevant
to the question, then say "I don't have information in the provided documents.."
                \n\nContext: {context}\n\nQuestion: {question}\n\nAnswer:'''
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": rag_prompt}], 
        max_tokens=200,
        temperature=0
    )
    return response.choices[0].message.content

##calling the functions
load_and_store('student_handbook.txt')
print("Document loaded and stored in vector database.")
print('type "exit" to quit.')
while True:
    query = input("Enter your question: ")
    if query.lower() == 'exit':
        break
    answer = ask(query)
    print("Bot Answer:", answer)
    print('\n')