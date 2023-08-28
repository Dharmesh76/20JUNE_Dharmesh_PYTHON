f1 = open('student.txt','r+')
read_line = f1.readlines()
file_contant = ""
for line in read_line:
    file_contant+=line
print(file_contant)    