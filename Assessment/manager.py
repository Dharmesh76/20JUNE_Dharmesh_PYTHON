import re
import pymysql
from datetime import date
class manager():
    usrnm:str
    usrpass:str
    lg_usrnm:str
    lg_usrpass:str
    try:
        dbconn = pymysql.connect(host="localhost",user="root",passwd="",database="medical management")
    except Exception as e:
        print(e)    
    cr = dbconn.cursor()    
    def reg(self):
            c = open("Manager_usrpass.txt","a")
            print("\t(Registration Username should contain atleast one capital,Numeric and small character)")
            self.usrnm = input("Enter Username :")
            usrnm_pattern = r"(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])"
            vali_usr = re.match(usrnm_pattern,self.usrnm)
            if vali_usr:
                f=open("Manager_usrpass.txt",'r')
                lines = f.readlines()
                for line in lines:
                    stored_usrnm = line.split(":")[0]
                    if self.usrnm == stored_usrnm:
                        print("username already exists Enter")
                        manager.reg(self)

                    else:
                        pass

            else:
                print("Enter Valid User Name")
                manager.reg(self)
    
    def password(self):
            print("\t(Password Should contain atleast one special character one Capital and one small)")
            self.usrpass = input("Create a Password :")
            if len(self.usrpass) < 6:
                print("Password length should be 6 or more")
                manager.password(self)
            else:    
                pass_pattern = r"(?=.*[A-Z])(?=.*[0-9])(?=.*[a-z])(?=.*\W)"
                valid_pass = re.match(pass_pattern,self.usrpass)
                if valid_pass:
                    re_pass = input("Re-Enter Password :")
                    if self.usrpass == re_pass: 
                        m=open("Manager_usrpass.txt",'a')
                        m.write(f"{self.usrnm}:{self.usrpass}\n")
                        print("Registration successfull")
                    else:
                        print("Password didn't Match")
                        manager.password(self)    
                else:
                    print("Enter Strong Password")
                    manager.password(self)    
    
    def lgusrnm_fn(self):
        self.lg_usrnm = input("Enter Your User Name :")
        l=open("Manager_usrpass.txt",'r')
        lines = l.readlines()
        for line in lines:
            stored_usrnm = line.split(":")[0]
            if self.lg_usrnm == stored_usrnm:
                pass
            else:
                print("User Name Not Registered please enter valid username")
                print("\t1.For Retry")
                print("\t2.For Registration")
                ch = int(input("Enter Your Choice :"))
                if ch == 1:
                    manager.lgusrnm_fn(self)
                if ch == 2:
                    manager.reg(self)
                    manager.password(self)    

    def lgpass_fn(self):
        self.lg_usrpass = input("Enter Your Password :")
        p=open("Manager_usrpass.txt",'r')
        lines = p.readlines()
        for line in lines:
            stored_pass = line.strip().split(":")[1]
            if self.lg_usrpass == stored_pass:
                pass
            else:
                print("Incorrect password Enter Correct password")
                manager.lgpass_fn(self)

    def add_medicine(self):
        medi_name = input("Enter the name of medicine :")
        medi_qty = input("Enter Quantity of medicine:")
        medi_added = input("Enter Added by :")
        medi_price = int(input("Enter the price of medicine :"))
        t_date = date.today()
        medi_date = t_date.strftime("%d/%m/%Y")
        try:
            add_medi = f"insert into medicine(name,date,qty,AddedBY,price)values('{medi_name}','{medi_date}','{medi_qty}','{medi_added}',{medi_price})"
            self.cr.execute(add_medi)
            self.dbconn.commit()
            print("Medicine Added Succesfull...")
            

        except Exception as e:
            print(e)

        print("\t1.Add More")
        print("\t2.Back")
        n = int(input("Enter Your choice :"))
        if n==1:
            manager.add_medicine(self)
        elif n == 2:
            manager.manager_choice(self)


    def view_medicine(self):
        try:
            view = "select * from medicine"        
            self.cr.execute(view)
            data = self.cr.fetchall()
            for i in data:
                print(i)
            ch = input("Press Enter For Back :")
            manager.manager_choice(self)    
        except Exception as e:
            print(e)        

    def delete_medi(self):
        n = int(input("Enter the SR no of medicine:"))
        del_medi = f"delete from medicine where SRNO ={n}"
        try:
            self.cr.execute(del_medi)
            self.dbconn.commit()
            print("Medicine Deleted...")
            ch = input("Press Enter For Back :")
            manager.manager_choice(self)
        except Exception as e:
            print(e)    
    
    def manager_choice(self):
            print("\t1.Add Medicine")
            print("\t2.View All Medicine")
            print("\t3.delete Medicine")
            print("\t4.Exit")
            choice = int(input("Enter Your Choice :"))
            if choice == 1:
                manager.add_medicine(self)
            elif choice == 2:
                manager.view_medicine(self)
            elif choice == 3:
                manager.delete_medi(self)
            elif choice == 4:
                print("Thank You For Visit (:")    
            else:
                print("Invalid Choice!!")
                manager.manager_choice(self) 

    def mnget_choice(self):
        print("\t1.Regstration If You Are New User")
        print("\t2.Login")
        ch = int(input("Enter Your Choice :"))
        if ch == 1:
            manager.reg(self)
            manager.password(self)
            manager.manager_choice(self)
        if ch == 2:
            manager.lgusrnm_fn(self)
            manager.lgpass_fn(self)
            manager.manager_choice(self)    

                               
        


        


