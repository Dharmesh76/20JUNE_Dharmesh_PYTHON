class area_rectangle:
    length:float
    width:float
    
    def getdata(self):
        self.length = float(input("Enter Length of rectangle :"))
        self.width=float(input("Enter Width of rectangle :"))
    
    def area_rec(self):
        area = self.length * self.width
        print("area of rectangle is :",area)

a = area_rectangle()
a.getdata()
a.area_rec()
