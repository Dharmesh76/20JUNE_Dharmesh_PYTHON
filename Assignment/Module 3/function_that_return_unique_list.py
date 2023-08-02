def unique_elements(list):
    list = set(list)
    print(list)

list = []
n = int(input("Enter the number of elements :"))
for i in range (n):
    x = input("Enter your elements :")
    list.append(x)
print("Noramal list :",list)
unique = unique_elements(list)