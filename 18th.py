l1=[54,53,2,1,45,65,788,34]
def selection(l):
    length=len(l)
    for i in range(length-1):
        for j in range(i+1,length):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
    return l
print(selection(l1))
