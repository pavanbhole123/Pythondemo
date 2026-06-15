from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()  # Load environment variables from .env file
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)
response = client.chat.completions.create(
  model="llama-3.1-8b-instant",
  messages=[
    {"role": "system", 
     "content": "You are friendly tutor for polytechnic students. use simple language to explain the concepts."
     },
    {"role": "user", 
     "content": "What is the difference between a capacitor and an inductor? in 4 bullet points"
     },  
  ],
  max_tokens=400,
  temperature=0.5
)
print(response.choices[0].message.content)
print("token used: ", response.usage.total_tokens)