n = int(input("Enter the range of Fibonocci series :"))
a = 0
b = 1
for i in range (0,n,1):
  if i == 0:
    print("0",end =" ")
  elif i == 1:
    print("1",end =" ")
  else :
    c = a + b
    a = b
    b = c
    print(c,end =" ")
print()    
