l1=[1,34,5,6,4,388,9,9,7,6554]
l1.sort()
def bise(l1,e):
    x=len(l1)
    if x==0:
        return False
    elif x==1:
        return l1[0]==e
    else:
        x=x//2
        if l1[x]==e:
            return True
        elif l1[x]>e:
            return bise(l1[:x],e)
        else:
            return bise(l1[x:],e)

print(bise(l1,6554))
     
    

