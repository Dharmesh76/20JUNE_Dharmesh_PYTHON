"""The zip() function in Python is used to combine two or more iterables (such as lists, tuples, or other sequences) element-wise, creating an iterator of tuples where the first item in each passed iterator is paired together, the second item in each passed iterator is paired together, and so on. In other words, it "zips" together corresponding elements from multiple iterables into a single iterable.

The main purpose of using the zip() function is to iterate over multiple sequences simultaneously and process their elements together. Here are a few common use cases for the zip() method:

Iterating over Multiple Lists Simultaneously:
You can use zip() to iterate over multiple lists or other sequences in parallel, processing corresponding elements together."""

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 28]

for name, age in zip(names, ages):
    print(name, age)

"""Creating Dictionaries:
You can use zip() to combine two lists into a dictionary, where one list contains keys and the other contains values."""
keys = ['a', 'b', 'c']
values = [1, 2, 3]

my_dict = dict(zip(keys, values))
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

"""keys = ['a', 'b', 'c']
values = [1, 2, 3]

my_dict = dict(zip(keys, values))
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}
"""