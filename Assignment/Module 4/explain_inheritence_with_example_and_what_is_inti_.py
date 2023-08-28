"""Inheritence Is fundamental concept of oop it allows you to inherit 
   attributes one class to another it is call inheritence.
"""

# Example
class student():
    
    stid:int
    stnm = ""

class teacher(student):
    
    def getdata(self):
        self.stid = int(input("Enter Student id :"))
        self.stnm = input("Enter Student name :")

    def printdata(self):
        print("id =",self.stid)
        print("Name =",self.stnm)

t1 = teacher()
t1.getdata()
t1.printdata()            

# Q. What is __init__ in python

""" intializ is also known AS CONSTRUCTOR and its called by default when you create object of class
    the purpose of int is initialize the attributes of the object and set its initial state.
"""

