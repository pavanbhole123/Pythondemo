#######
"""COnversation history pattern
we will use list to maintain history
1)for each turn of user we will save the user prompot to list
2)will send whole history to API
3)again we will append the response to list 
4)repeat


looping to make seesion active
1.intialise ssytem prompt
2.while True
2.get user input 
3.if "yes" will continue else will stop 
4.append user meaasge list
5.call api with full message 
6.response will add  to list
7.print reply
"""
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
print("""AI TUTOR CHATBOT""")
print("type 'quit' to exit")
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)
#system prompt
message=[{
    'role':'system',
    'content':'''you are friendly tutor for indian enginnering students
                keep answers in 100 words.
                Ask follow up questions for deepan learning
                be simple for student
    '''
}]
while True:
    user_prompt=input('user prompt: ').strip()
    if not user_prompt:
        continue
    if user_prompt.lower() in ['quit','bye']:
        print('BYE')
        break

    message.append({'role':'user','content':user_prompt})
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=message,
        max_tokens=200,
        temperature=0.7
    )
    reply = response.choices[0].message.content
    message.append({'role':'assistant','content':reply})
    print(f'AI response:{reply}')
