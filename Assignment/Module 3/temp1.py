my_list = {'a':1,'b':5,'c':7,'d':4,'e':8}
first = my_list['a']
b=[]
second = 0
third = 0
for i in my_list.values():
    if i > first:
        third = second
        second = first
        first = i
b.append(first)
b.append(second)
b.append(third)
print(b)        