from datetime import datetime
def customer_panel(fruit):
    wallet = 1000
    cost=0
    print("\t\tWELCOME TO FRUIT MARKET\n")
    print("\t\t1)See Wallet and Purchase Fruit")
    print("\t\t2)Exit")
    choice = int(input("Enter Your choice :" ))
    def see_purchase():
        nonlocal wallet
        nonlocal cost
        print("1) For Purchase Fruit")
        print("2) See Wallet")
        print("3) For Back")
        ch = int(input("Enter Your Choice :"))
        if ch == 1:
            print(fruit)
            buy_fruit = input("Enter The Name Of Fruit You Want To Buy :")
            if buy_fruit in fruit:
                qty_fruit = int(input("Enter Quantity You Want To Buy(In Kg) :"))
                cost +=fruit[buy_fruit]['price']*qty_fruit
            if wallet < cost:
                print("\t\tYou Don't Have Sufficient Money")
                print("\t\tPlease Select other Fruit Or Dercrease Quantity ")
                cost=0
                see_purchase()
            if qty_fruit > fruit[buy_fruit]['qty']:
                print("\n\t.Quantity Of Fruit Is Less Than You Want")
                print("\t.Enter The Available Quantity\n")
                qty_fruit=0
                see_purchase()
            else:
                fruit[buy_fruit]['qty']-=qty_fruit
                if fruit[buy_fruit]['qty']==0:
                    del fruit[buy_fruit]
                wallet -= cost
                print("Your Wallet amount is :",wallet)
                my_time = datetime.now()
                hour = my_time.hour
                minute = my_time.minute
                second  = my_time.second
                day = my_time.day
                month = my_time.month
                year = my_time.year

                f1 = open('Transaction.txt','a')
                print("\n")
                f1.write(f"DATE:-{day}/{month}/{year} TIME:-{hour}:{minute}\n")
                f1.write(f"Purchased fruit:{buy_fruit}\n")
                f1.write(f"Quantity:{qty_fruit}\n")
                f1.write(f"Recevied Amount (Rupees):{cost}\n")
                f1.write("\n")
                print("Thank You For Purchase :)\n")
                more = input("Press y For Back and n For Main Menu:")
                while more == 'y':
                    see_purchase()
                if more == 'n':
                    customer_panel(fruit)    
                else:
                    print("Fruit is Not Available Please Choose Fruit Mentioned Below")
                    see_purchase()
        if ch == 2:
            print(wallet)
            wl_exit = input("Enter 'E' For Exit :")
            if wl_exit == 'e' or 'E':
                see_purchase()
            else:
                print("Enter Valid Option") 
                wl_exit = input(print("Enter 'E' For Exit :"))
                if wl_exit == 'e' or 'E':
                    see_purchase() 
        if ch == 3:
            customer_panel(fruit)                                  

         
        
    if choice==1:
        see_purchase()  
    elif choice == 2:
        print("\t\nThank You For Vist :) \n")
        