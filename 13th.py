class fraction(object):
    def __init__(self,num,den):
        self.num=num
        self.den=den
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    def __add__(self,other):
        add_den=other.den*self.den
        add_num=((add_den//self.den)*self.num)+((add_den//other.den)*other.num)
        return str(add_num)+"/"+str(add_den)
    def __sub__(self,other):
        sub_den=other.den*self.den
        sub_num=((sub_den//self.den)*self.num)-((sub_den//other.den)*other.num)
        return str(sub_num)+"/"+str(sub_den)
    def get_num(self):
        return self.num
    def get_den(self):
        return self.den
    def float_conversion(self):
        return self.get_num()/self.get_den()
    def __lt__(self,other):
            return self.float_conversion()<other.float_conversion()
    def __gt__(self,other):
        return self.float_conversion()>other.float_conversion()
x=fraction(5,8)
y=fraction(4,8)
print(x)
print(x+y)
print(y-x)
print(y.float_conversion())
print(x<y)
print(y<x)
print(x>y)
print(y>x)