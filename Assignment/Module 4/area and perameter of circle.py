class circle:
    pi=3.14
    radius:float
    
    def get_radius(self):
        self.radius=float(input("Enter radius of circle :"))
    
    def area_circle(self):
        area = self.pi * self.radius * self.radius
        print("Area Of circle is :",area)
    
    def perimeter_circle(self):
        perimeter = 2 * self.pi * self.radius
        print("Perimeter of circle :",perimeter)

c = circle()
c.get_radius()
c.area_circle()
c.perimeter_circle()

        
