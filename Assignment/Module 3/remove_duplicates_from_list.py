list = ["python","java","c","c++","python","java"]
string = []
for i in list:
    if i not in string:
        string.append(i)
print("List after remove duplicates :",string)


