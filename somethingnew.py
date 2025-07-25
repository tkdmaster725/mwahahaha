import math
class yeah:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self,point):
        return math.sqrt(((point.x-self.x)**2)+((point.y-self.y)**2))
    
class shape:
    def vertices(self):
        return self.vertices
    def area(self):
        return 5
    def numvertices(self):
        return len(self.vertices)
    def perimeter(self):
        return
    
class rectangle(shape):
    def __init__(self, a,b,c,d):
        self.vertices = [a,b,c,d]
    
    def area(self):
        return self.vertices[0].distance(self.vertices[1]) * self.vertices[0].distance(self.vertices[3])
    def perimeter(self):
        return self.vertices[0].distance(self.vertices[1]) + self.vertices[0].distance(self.vertices[1]) + self.vertices[0].distance(self.vertices[3]) + self.vertices[0].distance(self.vertices[3])
    def numvertices(self):
        return super().numvertices()
class triangle(shape):
    def __init__(self, a,b,c):
        self.vertices = [a,b,c]
    def area(self):
        return (self.vertices[0].distance(self.vertices[1]) * self.vertices[1].distance(self.vertices[2]))/2
    def perimeter(self):
        return self.vertices[0].distance(self.vertices[1]) + self.vertices[1].distance(self.vertices[2]) + self.vertices[2].distance(self.vertices[0])

e=yeah(3,0)
f=yeah(0,0)
g=yeah(0,3)
h=yeah(3,3)

myrectange = rectangle(e,f,g,h)
print(myrectange.perimeter())
print(myrectange.get_super_area())