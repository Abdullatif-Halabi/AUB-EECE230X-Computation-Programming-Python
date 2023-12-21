class Vector(list):
    def __init__(self,other):
        assert len(other)!=0, "Invalid Input!"
        for e in other:
            assert type(e)==int or type(e)==float, "Invalid Input!"
        list.__init__(self,other)

    def __str__(self):
        b=''
        for i in self:
            b += str(i)+','
        return f'<{b[:-1]}>'

    def __add__(self,other):
        assert len(self) == len(other) , 'Inavalid Input!'
        return Vector([x1+x2 for x1,x2 in zip(self, other)])
    
    def __sub__(self,other):
        assert len(self) == len(other) , 'Inavalid Input!'
        return Vector([x1-x2 for x1,x2 in zip(self, other)])

    
    def __mul__(self,other):
        assert len(self) == len(other) , 'Inavalid Input!'
        return sum([x1*x2 for x1,x2 in zip(self, other)])

    
    def __neg__(self):
        return Vector([-x for x in self])

    
    def norm(self):
        sumSquared = 0
        for i in self:
            sumSquared += i**2
        return sumSquared**0.5
    
def zeros(n):
    vect = [0]*n
    return Vector(vect)
def ones(n):
    vect = [1]*n
    return Vector(vect) 
    


# import copy
# v = Vector([1,2.3])
# w = zeros(5)
# u = ones(2)
# print(v)
# print(w)
# print(v[1])
# print(v+v+v)
# print(v*u)
# print(v.norm())
# w[2]=3.5
# v = copy.deepcopy(w)
# print(v)
# print(-v)
# w[0]=15.5
# w[4]=-12
# print(w-v)
# print(-w+v)