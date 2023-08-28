file = open('student.txt','r+')
line = file.readlines()
count = 0
for lines in line:
    count+=1
print(count)    