class Animal(object):
    def __init__(self,age,):
        self.name=None
        self.age=age
    def get_age(self):
        return self.age
    def set_age(self,x):
        self.age=x
    def set_name(self,new_name=''):
        self.name=new_name
    def get_name(self):
        return self.name
    def __str__(self):
        return "Name: "+str(self.get_name())+", "+"age: "+str(self.get_age())
x=Animal(23)
print(x)
x.set_age(12)
x.set_name("Rubby")
print(x)

class Cat(Animal):
    def __init__(self,age,name=None):
        Animal.__init__(self,age)
        Animal.set_name(self,name)
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat: "+str(self.name)+", Age: "+str(self.age)
    
cat_var=Cat(12,"Tuffy")
cat_var.set_age(5)
print(cat_var)
cat_var.speak()


class Rabbit(Animal):
    def speak(self):
        print("meep")
    def __str__(self):
        return "rabbit: "+str(self.name)+", Age: "+str(self.age)

class Person(Animal):
    def __init__(self,age,name=None):
        Animal.__init__(self,age)
        Animal.set_name(self,name)
        self.friends=[]
    def add_friends(self,x):
        self.friends.append(x)
    def get_friends(self):
        return self.friends
    def speak(self):
        print("Hello")
    def __str__(self):
        return "Person: "+str(Animal.__str__(self))
x=Person(25)
x.set_name("ANIL")
print(x)


        

