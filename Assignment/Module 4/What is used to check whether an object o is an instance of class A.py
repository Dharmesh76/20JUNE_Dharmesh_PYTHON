class A():
    def get_data(self):
        stnm = input("Enter the name of student :")
        stid = int(input("Enter the id of student :"))
        print("Name :",stnm)
        print("Id :",stid)

o = A()
if isinstance(o,A):
    print("O is instance of class A")
else:
    print("O is not an instance of class of A")            