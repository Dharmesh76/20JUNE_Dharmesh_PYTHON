str = input("Enter your string :")
if len(str)<2:
    print(str)
else:
    print("New string is :",str[:2]+str[-2:])
