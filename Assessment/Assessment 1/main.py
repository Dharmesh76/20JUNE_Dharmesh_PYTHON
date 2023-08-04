from fruit_manager import manager_panel
from customer import customer_panel
def main():
    fruit = {'apple':{'qty':2,'price':100},'banana':{'qty':5,'price':80},'mango':{'qty':3,'price':40}}
    print("WELCOME TO FRUIT MARKET\n")
    print("\t\t1) For Manager")
    print("\t\t2) For Customer")
    print("\t\t3) Exit")
    choice = int(input("Enter Your Choice :"))
    if choice == 1:
        manager_panel(fruit)
    if choice == 2:
        customer_panel(fruit)
    if choice == 3:
        print("Tnak You :)")
    else:
       
        main()
main()        


 

