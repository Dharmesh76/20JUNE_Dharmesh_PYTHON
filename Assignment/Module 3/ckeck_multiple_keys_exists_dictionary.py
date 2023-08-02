my_dict = {"a":1,"b":2,"c":3,"d":4,"e":5}
key_1 = input("Enter your 1 key to check existancy in dictionary:")
key_2 = input("Enter your 2 key to check existancy in dictionary:")
if key_1 in my_dict.keys():
    if key_2 in my_dict.keys():
        print("Both keys are in dictionary")
    else:
        print("Key 1 is exists in dictionary")
elif key_2 in my_dict.keys():
    print("Key 2 is exists in dictionary")
                
    