my_tuple = ("python","java","c","c++","python","java")
temp = []
repeated_tuple = []
for i in my_tuple:
    if i not in temp:
        temp.append(i)
    else:
        repeated_tuple.append(i)        
print("Repeated item in tupel :",tuple(repeated_tuple))