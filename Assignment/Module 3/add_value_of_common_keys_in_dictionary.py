d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'c':400}
dict = {}
for i in d1.keys():
    if i in d2.keys():
        sum = d1[i]+d2[i]
        dict[i]=sum
print(dict)
        
