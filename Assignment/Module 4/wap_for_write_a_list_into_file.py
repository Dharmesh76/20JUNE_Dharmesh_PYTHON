list = ["red","green","black","orange","white","gray","blue","yellow"]
f1 = open('list.txt','a')
for word in list:
    f1.write(word)
    f1.write("\n")
f2 = open('list.txt','r+')
lines = f2.readlines()
for line in lines:
    print(line)
