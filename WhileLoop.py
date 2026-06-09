""" count = 0
while count < 5: #0<5=true #1<5=true 2<5=true,5<5
    if count == 3:
        break 
    print(count) #0,1,2,3,4
    count = count + 1 #4,5 """
count = 0
while count < 5: #0<5=true #1<5=true 2<5=true,5<5
    if count == 3:
        count = count + 1
        continue 
    print(count) #0,1,2,3,4
    count = count + 1 #4,5