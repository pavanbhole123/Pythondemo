# ==,!=,<,>,<=,>=
age =int(input('age: '))
if age == 18:
    print('You are 18 years old.')
if age != 18:
    print('You are not 18 years old.')
if age < 18:
    print('You are not 18 years old.')
if age > 18:
    print('You are older than 18.')
if age <= 18:
    print('You are not older than 18.')
if age >= 18:
    print('You are 18 or older.')
elif age > 18:
    print('You are older than 18.')