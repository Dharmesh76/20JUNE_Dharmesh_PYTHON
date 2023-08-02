def common_elements(list1,list2):
    count=0
    for i in list1:
        for j in list2:
            if i == j:
                count+=1
    if count>=1:
        print("true")

list1 = ["java","c","c++"]
list2 = ["python","java","flutter","js"]
common_elements(list1,list2)