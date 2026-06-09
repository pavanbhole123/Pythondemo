students={'Raj': 85, 'Priyanka': 92, 'Amit': 78, 'Priya': 88}
#print(students)
#print(students['Raj'])
#append
students['Mahesh'] = 90
#update
students['Amit'] = 80
#students.pop("Priya")
#print(students)
students=[{'Raj': 85, 'Priyanka': 92, 'Amit': 78, 'Priya': 88}, {'Mahesh': 90}]
""" for key in students:
    print(key)
for value in students.values():
    print(value) """
print(students.keys())
print(students.values())
for key, value in students.items():
    
    print(key, value)