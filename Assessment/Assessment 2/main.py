from manager import *
from admin import *
class main(admin,manager):
    def main_fn(self):
        print("Welcome To Mixon Pharmacy")
        print("\t1.Manager")
        print("\t2.Admin")
        print("\t3.Exit")
        choice = int(input("Enter Your Choice :"))
        if choice == 1:
            manager.mnget_choice(self)
        elif choice == 2:
            admin.get_choice(self)
        elif choice == 3:
            print("Thank You For Visite (:")    
        else:
            print("Invalid Choice !!")
            main.main_fn(self)

m = main()
m.main_fn()

            
        
