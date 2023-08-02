my_list = [(1, 2, 3), (4, 5, 6), ()]
for i in my_list:
    if len(i) <= 0:
        my_list.remove(i)
    else:
        pass
print(my_list)
    
