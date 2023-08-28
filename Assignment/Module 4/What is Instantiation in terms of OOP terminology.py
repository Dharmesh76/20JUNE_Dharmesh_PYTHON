"""When you instantiate a class, you're essentially creating a unique object that follows
the characteristics and behaviors defined by that class.
This instance will have its own set of attributes with specific values 
and can execute the methods defined in the class."""
class student():
    def __init__(self) -> None:
        stid = input("Enter The id of students :")
        stnm = input("Enter The Name of student :")
        print("Name = ",stnm)
        print("Id =",stid)
s = student()        