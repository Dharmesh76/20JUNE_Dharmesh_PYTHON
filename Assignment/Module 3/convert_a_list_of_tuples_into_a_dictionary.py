list = [(1, 2, 3),(4, 5, 6),(7, 8, 9)]
key_list=[1,2,3]
my_dict = {}
for i in range (0,4):
    for j in range (i):
        my_dict[i]=list[j]
print(my_dict)        

