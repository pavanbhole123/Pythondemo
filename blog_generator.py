'''
Input:- topic,length and tone
prompt building:-
                you are experts blog writer,
                write a {length}-word blog post about:{topic},
                Tone:{tone}
                Structure:-
                    - Title
                    - Introduction
                    -3-4 sections with clear headings
                    - practical examples
                    - Strong conclusions
                Make it engaging and easy to read 
AI generation
output

'''
from openai import OpenAI
from dotenv import load_dotenv
import os
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)
def gererate_blog(topic,length,tone):
    prompt=f'''You are experts blog writer,
                write a {length}-word blog post about:{topic},
                Tone:{tone}
                Structure:-
                    - Title
                    - Introduction
                    -3-4 sections with clear headings
                    - practical examples
                    - Strong conclusions
                Make it engaging and easy to read '''
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{'role':'user','content':prompt}],
        temperature=0.7,
        max_tokens=1200
    )
    final_response = response.choices[0].message.content
    return final_response

print("AI BLOG GENERATOR")
topic = input("Enter blog topic: ")
tone = input("Enter the tone like(friendly,professionl,funny):  ")
length = input("Length(small/medium/large)").lower()
length_map = {'small':200,'medium':500,'long':800}
word_count = length_map.get(length,500)
print("Generating blog")
blog = gererate_blog(topic,word_count,tone)
print('\n')
print(blog)

