#define class with class (name)
class sum :
    a:int
    b:int
    def getvalue(self):
        self.a = int(input("Enter value of A:"))
        self.b= int(input("Enter value of B :"))

    def sum_of_value(Self):
        sum = Self.a + Self.b
        print(sum)

s = sum()
s.getvalue()
s.sum_of_value()
        