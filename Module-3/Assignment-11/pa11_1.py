class Complex(object):

    def __init__(self , x=0 , y=0):
        assert isinstance(x, (int, float)) and isinstance(y, (int, float)), "Bad Input!"
        self.x = x
        self.y = y
    def conj(self):
        return Complex(self.x,-self.y)
    def norm(self):
        return (self.x **2 + self.y **2)**0.5
    
    def __add__(self , other):
        return Complex(self.x + other.x , self.y + other.y )
    def __sub__(self , other):
        return Complex(self.x - other.x , self.y - other.y )
    def __mul__(self,other):
        return Complex(self.x * other.x - self.y * other.y , self.x * other.y + self.y * other.x )
    def __truediv__(self,other):
        denom = (other.x **2 + other.y**2)
        return Complex( (self.x * other.x + self.y * other.y)/denom , (self.y * other.x - self.x * other.y)/denom )

    def __neg__(self):
        return Complex(-self.x , -self.y) 

    def __str__(self):
        return str(complex(self.x , self.y))
    

# h = Complex('d' , 5)
# r = Complex(12)
# z = Complex(1.5,2)
# t = Complex(2.2,3)
# print(r)
# print(z+t)
# print(-z)
# print(z*t)
# print(z/t)
# print(z.conj())
# print(z.norm())