list1 = [20,10,41,45,60,100]
largest = 0
small = list1[0]
sum = 0
for i in list1:
    sum +=i
    if i < small:
        small = i
    else :
        pass   
    if i > largest:
        largest = i
    else:
        pass
print("Smallest number is :",small)
print("Largest number is :",largest)
print("Sum of list is :",sum)