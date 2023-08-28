try:
    number = int(input("Enter Odd Number only :"))
    if number % 2 == 0:
       raise ValueError("Entered Number is even number plz enter odd number")
    else:
       print("Value Entered Successfully ")
        
except ValueError as e:
 print(e)        
