class Point(object):
    def __init__(p,x=0,y=0):
        assert isinstance(x, (int, float)) and isinstance(y, (int, float)), "Bad Input!"
        p.x = x
        p.y = y
 
    def __str__(p):
        return  f'({p.x} , {p.y})'
    

class Rectangle(object):
    def __init__(R , p=Point(), q=Point()):
        assert isinstance(p, Point) and isinstance(q, Point) and p.x<=q.x and p.y<=q.y, "Bad Input!"
        R.p = p
        R.q = q
        
    def __str__(R):
        return f"(p=({R.p.x},{R.p.y}) ,q=({R.q.x},{R.q.y}))"
    
    def height(R):
        return R.q.y - R.p.y
    def width(R):
        return R.q.x - R.p.x
    def perimeter(R):
        return (R.height() + R.width())*2
    def area(R):
        return R.width() * R.height()
    def contains(R,pt=Point()):
        assert isinstance(pt , Point), "Bad Input!"
        return R.p.x<= pt.x <=R.q.x  and  R.p.y<= pt.y <=R.q.y
    

R = Rectangle(p=Point(1,2), q=Point(3.2 ,4))
print(R)
print(R.width())
print(R.height())
print(R.area())
print(R.perimeter())
print(R.contains(Point(1.5,3)))
print(R.contains(Point(10.5,3)))

