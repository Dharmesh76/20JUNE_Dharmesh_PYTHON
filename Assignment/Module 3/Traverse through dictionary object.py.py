#we can traverse in dictionary object with many type of methods 
# 1.traverse through keys
# 2.traverse through values
# 3.traverse through items(keys and values)
# 1.traverse through keys
my_dict = {"a":1,"b":2,"c":3,"d":4}
for key in my_dict.keys():
    print("keys =",key)

# 2.traverse through value
for value in my_dict.values():
    print("values=",value)

#3. traverse through items
for keys,values in my_dict.items():
    print(f"keys ={keys} || values ={values}")
  