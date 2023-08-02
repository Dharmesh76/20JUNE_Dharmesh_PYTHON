list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_list = []
new_value = 45
for i in list:
    modified_tupl = i[:-1]+(new_value,)
    new_list.append(modified_tupl)
print(new_list)    