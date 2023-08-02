list = ["mango","banana","lichi","orange","pinapple"]
sub_list = ["mango","lichi","java"]
count = 0
for i in sub_list:
    if i in list:
        count+=1
    else:
        pass
  
if count == len(sub_list):
    print("Sub list contain in list")
else:
    print("Sub list not contain in list")    
