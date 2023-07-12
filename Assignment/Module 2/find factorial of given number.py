n = int(input("Enter the number for factoria :"))
fact = 1
for i in range(n,1,-1):
    fact = fact * i
print("factorial of Given number :",fact)    