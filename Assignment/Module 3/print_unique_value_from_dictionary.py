my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 3, 'e': 2}
unique_value = set()
for value in my_dict.values():
    unique_value.add(value)
print("Unique value of dictionary is:",unique_value)
