from math import pi
class Point(object):
    def __init__(p,x=0,y=0):
        assert isinstance(x, (int, float)) and isinstance(y, (int, float)), "Bad Input!"
        p.x = x
        p.y = y
 
    def __str__(p):
        return f'({p.x} , {p.y})'
       
class Circle(object):
    def __init__(C,center=Point(),radius=1):
        assert isinstance(center , Point) and isinstance(radius , (int,float)), "Bad Input!"
        C.center = center
        C.radius = radius
    def __str__(C):
        return f"(({C.center.x},{C.center.y}),{C.radius})"
    
    def diameter(C):
        return  2* C.radius
    def perimeter(C):
        return  pi*2*C.radius
    def area(C):
        return pi*(C.radius**2)
    def contains(C,pt):
        assert isinstance(pt , Point) , "Bad Input!"
        return True if ((C.center.x - pt.x)**2 + (C.center.y - pt.y)**2) <= C.radius**2 else False
    def intersect(C,other):
        assert isinstance(other,Circle),'Bad Input!'
        x1 = C.center.x
        y1 = C.center.y
        x2 = other.center.x
        y2 = other.center.y
        return True if C.radius+other.radius >= ((x1-x2)**2 + (y1-y2)**2)**0.5 else False
    

# C1 = Circle()
# C2 = Circle(Point(1,0.5),0.75)
# C3 = Circle(Point(10,5),2)
# print(C1)
# print(C2)
# print(C3)
# print(C1.diameter())
# print(C2.perimeter())
# print(C3.area())
# print(C1.contains(Point(0.5,0.5)))
# print(C1.contains(Point(5,5)))
# print(C1.intersect(C2))
# print(C1.intersect(C3))