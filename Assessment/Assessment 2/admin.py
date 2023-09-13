import re
import pymysql 
class admin():
    usrnm:str
    usrpass:str
    lg_usrnm:str
    lg_usrpass:str
    
    dbcon = pymysql.connect(host='localhost',user='root',passwd='',database='medical management')
    print("Database Connected Succesfull !")
    cur = dbcon.cursor()

    def reg(self):
        c = open("Admin_usrpass.txt","w")
        print("\t(Registration Username should contain atleast one capital,Numeric and small character)")
        self.usrnm = input("Enter Username :")
        usrnm_pattern = r"(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])"
        vali_usr = re.match(usrnm_pattern,self.usrnm)
        if vali_usr:
            f=open("Admin_usrpass.txt",'r')
            lines = f.readlines()
            for line in lines:
                stored_usrnm = line.split(":")[0]
                if self.usrnm == stored_usrnm:
                    print("username already exists")
                    admin.reg(self)
                else:
                    pass

        else:
            print("Enter Valid User Name")
            admin.reg(self)
    
    def password(self):
        print("\t(Password Should contain atleast one special character one Capital and one small)")
        self.usrpass = input("Create a Password :").strip()
        if len(self.usrpass) < 6:
            print("Password length should be 6 or more")
            admin.password(self)
        else:    
            pass_pattern = r"(?=.*[A-Z])(?=.*[0-9])(?=.*[a-z])(?=.*\W)"
            valid_pass = re.findall(pass_pattern,self.usrpass)
            if valid_pass:
                re_pass = input("Re-Enter Password :").strip()
                if self.usrpass == re_pass: 
                    m=open("Admin_usrpass.txt",'a')
                    m.write(f"{self.usrnm}:{self.usrpass}\n")
                    print("Registration successfull")
                else:
                    print("Password didn't Match")
                    admin.password(self)    
            else:
                print("Enter Strong Password")
                admin.password(self)    
    
    def lgusrnm_fn(self):
        self.lg_usrnm = input("Enter Your User Name :")
        l=open("Admin_usrpass.txt",'r')
        lines = l.readlines()
        for line in lines:
            stored_usrnm = line.split(":")[0]
            if self.lg_usrnm == stored_usrnm:
                pass
            else:
                print("\t1.Try again")
                print("\t2.If you are new user Regstration")
                ch = int(input("Enter Your Choice :"))
                if ch == 1:
                    admin.lgpass_fn(self)
                elif ch == 2:
                    admin.reg(self)
                    admin.password(self)    
                

    def lgpass_fn(self):
        self.lg_usrpass = input("Enter Your Password :")
        p=open("Admin_usrpass.txt",'r')
        lines = p.readlines()
        for line in lines:
            stored_pass = line.strip().split(":")[1]
            if self.lg_usrpass == stored_pass:
                pass
            else:
                print("Incorrect password Enter Correct password")
                admin.lgpass_fn(self)

    def view_manager(self):
        try:
            view = "select * from manager"
            self.cur.execute(view)
            data = self.cur.fetchall()
            for i in data:
                print(i)
        except Exception as e:
            print(e)    

        ch = input("Press Any Enter To Back :")
        admin.admin_choice(self)        


    def view_medicine(self):
        try:
            view = f"select SRNO,name,date,AddedBY from medicine"
            self.cur.execute(view)
            data =self.cur.fetchall()
            for i in data:
                print(i)
            ch = input("Press ENTER For back :")
            admin.admin_choice(self)  
        except Exception as e:
            print(e)

    def admin_choice(self):
        print("\t1.View Manager")
        print("\t2.View Medicine")
        print("\t3.Exit")
            
        ch = int(input("Enter your choice :"))
        if ch == 1:
                admin.view_manager(self)
        elif ch==2:    
                admin.view_medicine(self)
        elif ch==3:
            print("Thank For Visit (:")        
        else:
            print("Invalid Choice !!")
            admin.admin_choice(self)
        
            

    def get_choice(self):
        print("\t1.Registration")
        print("\t2.Login")
        choice = int(input("Enter Your Choice :")) 
        if choice == 1:
            admin.reg(self)
            admin.password(self)
            admin.admin_choice(self)
            
        elif choice == 2:
            admin.lgusrnm_fn(self)
            admin.lgpass_fn(self)
            admin.admin_choice(self)




                



        





