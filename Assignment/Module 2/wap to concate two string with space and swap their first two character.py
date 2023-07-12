str1 = input("Enter the first string :")
str2 = input("Enter the second string :")
if len(str1) >= 2 and len(str2) >= 2:
    newstr1 = str2[:2] + str1[2:]
    newstr2 = str1[:2] + str2[2:]
    result = newstr1 + " " + newstr2
    print("New string is :",result)
else:
    print("Your string must have minimum two character :")    
