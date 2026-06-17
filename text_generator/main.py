#text generator  example blog writing,draft email,production notes

#Application architecture
""" 
1)user input topic:type,audiance,etc
2)building of system prompt
3)openAPI call
4)get AI response
5)display on terminal
6)save to file  
"""
""""
prompt simple :write about solar energy
Role:"you are a professional content writer for Indian students"
Task:"write blog about solar enegy"
Audiance:"this is for indian farmer who are new to this concept"
Tone:"use friendly and simple tone"
format:"use small 3 sections"
Constraints:keep it under 300 words 
"""
""""
tempreture:It controls the randomness of AI api response
ranges between 0.0 to 2.0
0.0-0.3:-deterministic,factual mostly used for code generation
0.4-0.7:balanced mostly used for blogs,explanation,etc
0.8-1.0:creative user for poems, stories,etc
above 1.0:random wild not mostly used 
"""
"""
max_tokens:which control the Length of response and the cost
1 token = 3/4 of word ,100 tokens=75words 
for short response max_token should be 150 medium 400, long 1000
"""
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import re
import os 
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)
topic = input("Topic: ")
content_type= input("Type(article,summary,post,etc): ")
audience=input("Audience (beginer,expert,childern,noob): ")
tone=input("Tone (casual,formal,simple,fun,etc)")
system_prompt= f'''you are an expert {content_type} writer for indian audiance.
write a structured {content_type} on given topic.
Audience:{audience}
Tone:{tone}
keep it under 300 words 
'''
response = client.chat.completions.create(
  model="llama-3.1-8b-instant",
  messages=[
    {"role": "system", 
     "content": system_prompt
     },
    {"role": "user", 
     "content": f"write {content_type} about {topic} "
     },  
  ],
  max_tokens=400,
  temperature=0.7
)
result=response.choices[0].message.content

print(result)
filename=topic.lower()+".txt"
with open(filename,'w')as f:
    f.write(result)
print("response saved to file"+filename)