l1=[12,45,65,6,5,64,4]
def buble(l):
    length=len(l)-1
    while(length>0):
        for i in range(0,length):
            if l[i]>l[i+1]:
                l[i],l[i+1]=l[i+1],l[i]
            else:
                pass
        length=length-1
    return l
print(buble(l1))