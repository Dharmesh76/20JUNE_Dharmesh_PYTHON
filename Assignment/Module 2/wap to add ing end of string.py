str = input("Enter your string :")
if len(str) >= 3:
    if str[-3:] == 'ing':
        str += 'ly'
    else :
        str += 'ing'
    print(str)
else:
    print(str)