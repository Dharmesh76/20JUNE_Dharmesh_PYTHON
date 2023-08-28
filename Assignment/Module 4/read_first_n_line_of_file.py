f1=open('student.txt','r+')
#print(f1.readlines()[0])
n = int(input("Enter the number of lines you Want to print:"))
lines = f1.readlines()
for i in range(n):
    print(lines[i])