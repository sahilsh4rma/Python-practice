class int_collection(object):
    def __init__(self):
        self.vals=[]
    def insert(self,e):
        if e not in self.vals:
            self.vals.append(e)
    def remove(self,e):
        self.vals.remove(e)
    def member(self,e):
        return e in self.vals
    def __str__(self):
        representation=""
        for e in self.vals:
            representation=str(e)+", "+representation
        return "{"+representation+"}"
x=int_collection()
x.insert(1)
x.insert(5)
x.insert(5)
x.insert(4)
x.remove(4)
print(x)