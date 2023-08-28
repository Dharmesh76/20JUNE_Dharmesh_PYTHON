"""The finally block always excuted when try and exception block exists.
even if exception raise unexpected error occurance"""

try :
    a = int(input("enter Value of a :"))
    b = int(input("Enter value of b :"))
    sum = ("Sum =",a+b)
    print(sum)
except Exception as e:
    print("Error :",str(e))
finally:
    first = int(input("Enter first value :"))
    second = int(input("Enter Second Vlaue :"))
    multi = print("Multiplication =",first*second)    

