f1 = open('student.txt','a')
def appenddata():
    n=int(input("Enter the Number of studets :"))
    for i in range(n):
        id = int(input(f"Enter id Of student {i+1}:"))
        name = input(f"Enter Name Of Student{i+1}:")
        city = input(f"Enter city Of student {i+1}:")
        f1.write("\n")
        f1.write(f"ID = {id}\n")
        f1.write(f"NAME = {name}\n")
        f1.write(f"CITY = {city}\n")
        f2 = open('student.txt','r+')
        print(f2.read())

appenddata()
