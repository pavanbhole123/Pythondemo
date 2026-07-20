'''
function for api call
- summarise(study_material)
- make_quize(material)
- flashcrds
'''
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY", "ollama")
DEFAULT_MODEL = os.getenv("OLLAMA_MODEL", "llama3:latest")

client = OpenAI(
    base_url=OLLAMA_BASE_URL,
    api_key=OLLAMA_API_KEY
)

def ask_ai(prompt):
    response = client.chat.completions.create(
        model=DEFAULT_MODEL,
        messages=[{'role': 'user', 'content': prompt}],
        temperature=0.7,
        max_tokens=600
    )
    return response.choices[0].message.content
def summarise(material):
    result = ask_ai(f'Summarise this in 5 key points:\n{material}')
    print('\n---SUMMARY----\n'+result)
def make_quiz(material):
    result = ask_ai(f'Create 5 multiple-choice questions from the material:\n{material}')
    print('\n---QUIZ----\n'+result)
def flashcards(material):
    result = ask_ai(f'Create 5 flashcards as Question / Answer pairs ' f'for revision from:\n{material}')
    print('\n---FLASHCARDS---\n'+result)  

print("===AI Study Assistant===")
material = input('\nPaste your study material:\n')
while True:
    print(
        '''
        1. Summarise
        2. Generate Quiz
        3. Create Flashcards
        4. Exit
    '''
    )
    choice = input('choose (1 to 4)').strip()
    if choice == '1': summarise(material)
    elif choice == '2': make_quiz(material)
    elif choice == '3': flashcards(material)
    elif choice == '4': 
        print("Bye")
        break
    else:
        print("\nInvalid choice")

