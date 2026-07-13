'''
###user input
name,course/qulification,skills,experince,job_target,projects

##challenging part is propmpt
prompt:"You are a professional resume writer".
        "Create polished resume from the raw details".
        "IMPROVE the languge - use action verbs,professional pharsing".
        "Name":{name}
        Course:{course}
        Skills:{skills}
        Experinece:{Experinece}
        Target Role: {job_target}
        craete sections:Professional summary, Skills,Education,Experinece,prjects
        make it ready so the we can submit it
'''

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)
def generate_resume(data):
    prompt = f'''You are a professional resume writer".
        Create polished resume from the raw details.
        IMPROVE the languge - use action verbs,professional pharsing.
        Name:{data['name']}
        Course:{data['course']}
        Skills:{data['skills']}
        Experinece:{data['experience']}
        Target Role: {data['job_target']} 
        Create this sections:
        - PROFESSIONAL SUMMARY(3 Lines)
        - KEY Skills (bullet points)
        - EDUCATION
        - EXPERIENCE(with action verbs)
        - PROJECTS(with action verbs)
        format it cleanly and make it ready to submit
    '''
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}],
        temperature=0.5,
        max_tokens=500
    )
    return response.choices[0].message.content
def generate_cover_letter(data,company):
    prompt=f'''Write a prfessional cover letter for {data['name']}
            applying fro {data['job_target']} at {company},
            Use their backgound:{data['course']},skills:{data['skills']},
            experience: {data['experience']}
            keep it under 200 words ,make it professional..'''
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}],
        temperature=0.5,
        max_tokens=500
    )
    return response.choices[0].message.content

print("######AI Generator#####")
print('Enter your details')
data = {
    'name': input('Full name: '),
    'course': input('Course: '),
    'skills': input('Skills (comma seperated): '),
    'experience': input('Experinece(describe roughly): '),
    'job_target': input('Target Job Role: ')
}
#print('\n Building your resume...\n')
#resume = generate_resume(data)
##print(resume)
#print('=' * 50)
#filename = data['name'].lower().replace(' ','_')+'_resume.txt'
#with open(filename,'w',encoding='utf-8') as f:
#    f.write(resume)
#print(f'\n saved:{filename}')
company = input("enter the company name for cover letter")
letter=generate_cover_letter(data,company)
print('\n COVER LETTER  ')
print(letter)
