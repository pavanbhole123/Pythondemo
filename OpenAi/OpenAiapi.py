from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o-mini",
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