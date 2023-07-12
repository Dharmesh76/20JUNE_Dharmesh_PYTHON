"""#with temp variable
a = int(input("Enter value of a :"))
b = int(input("Enter value of b :"))
print("without swap")
print("a = ",a)
print("b = ",b)
temp = a
a=b
b=temp
print("after swap :")
print("a = ",a)
print("b = ",b)"""

#withput temp variable
a = int(input("Enter value of a :"))
b = int(input("enter value of b "))
print("Withput swap ")
print("a = ",a)
print("b = ",b)
a,b = b,a
print("after swap ")
print("a = ",a)
print("b = ",b)
