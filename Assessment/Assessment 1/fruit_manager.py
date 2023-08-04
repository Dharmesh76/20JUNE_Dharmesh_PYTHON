def manager_panel(fruit):
    print("\t\tFRUIT MARKET MANAGER\n")
    print("\t\t1) Add Fruit Stock")
    print("\t\t2) View Fruit Stock")
    print("\t\t3) Update Fruit Stock")
    print("\t\t4) Back\n")
    n = int(input("Enter Your Choice :"))
    #code for add fruit to store
    def add_fruit():

        print("\bADD FRUIT STOCK\n")
        num_fruit = int(input("Enter The Number of fruit you want to add :"))
        fruit_add = {}
        key = ['qty','price']

        for i in range(num_fruit):
            name_fruit = input("Enter Name Of Fruit :")
            if name_fruit in fruit:
                qty = int(input("Enter quantity of fruit :"))
                price = int(input("Enter the Price Of fruit :"))
                fruit[name_fruit]['qty']+=qty
                fruit[name_fruit]['price']=price
            else: 
                qty = int(input("Enter quantity of fruit :"))   
                price = int(input("Enter Price Of Fruit :"))
                fruit_add[key[0]]=qty
                fruit_add[key[1]]=price 
                fruit[name_fruit]=add_fruit

        print("\n\t\t FRUIT SUCCESFULLY ADDED....")
        more = input("\nFor Add More Press y Otherwise n :")

        if more == 'y':
            add_fruit()
        elif more == 'n':
            manager_panel(fruit)
        else:
            print("Enter Valid Choice")  
            more = input("\nFor More Performance Press y Otherwise n :") 

    #code for view stock
    def view_stock():
        print(fruit)
        more = input("\nFor Return To Main Menu Press 'Y' :")
        if more == 'y' or 'Y':
            manager_panel(fruit)
        elif more !='y' or 'Y':
            view_stock()
    #code for update stock    
    def update_stock():
        print("\t\t1. Update Fruit Quantity")
        print("\t\t2. Remove Fruit")
        print("\t\t3. Back")
        ch = int(input("Enter Your Choice :")) 
        if ch==1:
            remove_nm = input("Enter The Name Of Fruit You Want To Update Quantity :")
            if remove_nm not in fruit:
                print("Fruit Is Not Available :")
            else:    
                updated_quantity = int(input(f"Enter The New Quantity Of {remove_nm} :"))
                fruit[remove_nm]['qty']=updated_quantity
        elif ch == 2:
            rm_name = input("Enter The Name Of Fruit You Want To Remove :")
            if rm_name not in fruit:
                print("Entered Fruit Is Not Available")
            else:
                del fruit[rm_name]
                print("\t\t\nFruit Successfully Removed....")
        elif ch == 3:
            manager_panel(fruit)        
        else:
            print("enter Valid Option")
            update_stock()       
    if n==1:
            add_fruit()
    if n== 2:
            view_stock()
    if n==3:
            update_stock()
    if n==4:
            print("Thank you")
            
  

