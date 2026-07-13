####craete input
'''name,marks={'math',physics','chemistry',english','workshop'}
###grading system 
will take one function 
above 90 A+,between 80-90 A,between 70-80 B,between 60-70 C,F
###subject wise remark
generte_subject_wise_remark(score,subject)
###overall remark
generate_overall_remark(name,avg,grade)
then will generate a report card  for each student
'''
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
import csv
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)
#sample data
def getdatafromcsv(filepath):    
    students = []
    with open(filepath,newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        subjects = []
        for col in reader.fieldnames:
            if col!='Name':
                subjects.append(col)
        for row in reader:
            print(row)
            marks = {}
            for subject in subjects:
                marks[subject] = int(row[subject])
            students.append({'Name': row['Name'], 'Marks': marks})
        return students
def get_garde(avg):
    if avg >= 90: return 'A+'
    elif avg >= 80: return 'A'
    elif avg >= 70: return 'B'
    elif avg >= 60: return 'C'
    else: return 'F'
def generate_subject_remark(subject,score):
    prompt = (f'In ONE sentence, write a constructive remark for student who scored {score}/100 in {subject}'
              f'Be encouraging')
    r = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}], 
        max_tokens=60,
        temperature=0.5
    )
    return r.choices[0].message.content
def generate_overall_remark(name,avg,grade):
    prompt = (f'Write a 2-sentence encouraging overall academic comment for {name}'
              f'who scored an average of {avg:.1f}% (Grade {grade}).'
              f'Be motivating')
    r = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}], 
        max_tokens=80,
        temperature=0.5
    )
    return r.choices[0].message.content
os.makedirs('reports',exist_ok=True)
students = getdatafromcsv('C:\\Users\\Rutuja\\Downloads\\students.csv')
for student in students:
    name = student['Name']
    marks = student['Marks']
    avg = sum(marks.values())/len(marks)
    grade = get_garde(avg)
    print(f'Generating report for {name}...')
    lines = [
        f'STUDENT REPORT {name}',
        f'Average:{avg:.1f}% and Grade:{grade}',
        '',
        'Subject-wise Remarks:',      
    ]
    for subject, score in marks.items():
        remark = generate_subject_remark(subject,score)
        lines.append(f'{subject} ({score}):{remark}')
    lines = lines + ['','Overall Remark:',generate_overall_remark(name,avg,grade)]
    filename = 'reports/'+name.replace(' ','_')+'_'+'report'+'.txt'
    with open(filename,'w',encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'saved:{filename}')
print('report card generated')


