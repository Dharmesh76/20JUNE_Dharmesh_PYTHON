try :
    a = int(input("Enter the value of A :"))
    b = int(input("Enter the value of B :"))
    sum = a+b
    print(sum)
except Exception as e:
    print("An Error Occur :",str(e))
finally:
    x = int(input("Enter the value of X:")) 
    y = int(input("Enter the value of y:"))
    multi = x*y
    print(multi)       