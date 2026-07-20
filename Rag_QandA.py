'''
Load
chunk
embed
retrive 
generate

get_embedings,chunking,cosine_similarity,load_document,answer_question
'''
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("OPENAI_API_KEY")
    )
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

#get embiddings
def get_embeddings(texts):
    embeddings = model.encode(texts)
    return embeddings.tolist()
#cosine similarity
def cosine_similarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    norm_vec1 = sum(a * a for a in vec1) ** 0.5
    norm_vec2 = sum(b * b for b in vec2) ** 0.5
    return dot_product / (norm_vec1 * norm_vec2)
#chunking
def chunk_text(text,chunk_size=400,overlap=50):
    param = []
    for p in text.split('\n\n'):
        if p.strip():
            param.append(p.strip())
    if len(param) >= 3:
        return param
    chunks,start = [],0
    while start < len(text):
        chunks.append(text[start:start + chunk_size])
        start = start + chunk_size - overlap
    return chunks
# loading document
def load_document(filepath):
    if not os.path.exists(filepath):
        print(f'Error : file {filepath} not found')
        return None
    with open(filepath,'r',encoding='utf-8')as f:
        text = f.read()
    if not text.strip():
        print('Error: document is empty')
        return None
    chunks = chunk_text(text)
    print(f'loadded {len(chunks)} chunks')
    stored = []
    for c in chunks:
        stored.append({'text':c,'embedding':get_embeddings(c)})
    return stored
    #Answer question
def answer_question(queastion,stored):
    q_embeding =get_embeddings(queastion)
    scores = []
    for s in stored:
        scores.append(cosine_similarity(q_embeding,s['embedding']),s['text'])
    scores.sort(reverse=True)
    top_chunks = [v for k,v in scores[:2]]
    context = '\n\n'.join(top_chunks)
    prompt = f'''
            Asnswe the question USING ONLY the below context.
            If Answer is not there, say
            I dont have the information in document.
        context:{context}
        question:{queastion}
'''

    
    

    


