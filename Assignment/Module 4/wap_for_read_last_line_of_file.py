f1 = open('student.txt','r+')
read = f1.readlines()
print(read[-1])
f1.close()