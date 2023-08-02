def sort_dict_by_value(dictionary, descending=False):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=descending))
    return sorted_dict

# Sample dictionary
my_dict = {'apple': 3, 'banana': 1, 'cherry': 5, 'date': 2}

# Sorting in ascending order
sorted_ascending = sort_dict_by_value(my_dict)
print("Ascending Order:", sorted_ascending)

# Sorting in descending order
sorted_descending = sort_dict_by_value(my_dict, descending=True)
print("Descending Order:", sorted_descending)
