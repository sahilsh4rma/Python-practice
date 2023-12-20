class coordinate(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return "<"+str(self.x)+", "+str(self.y)+">"
    def dis(self,other):
        x_diff=(self.x-other.x)**2
        y_diff=(self.y-other.y)**2
        return (x_diff+y_diff)**0.5
c=coordinate(3,4)
o=coordinate(0,0)
print(c.dis(o))
print(c,o)
print(isinstance(c,coordinate))