l1=[1,34,5,6,4,388,9,9,7,6554]
l1.sort()
# def bise(l1,e):
#     x=len(l1)
#     if x==0:
#         return False
#     elif x==1:
#         return l1[0]==e
#     else:
#         x=x//2
#         if l1[x]==e:
#             return True
#         elif l1[x]>e:
#             return bise(l1[:x],e)
#         else:
#             return bise(l1[x:],e)

# print(bise(l1,6554))

def best_bisec(l1,e):
    def b(low,high,l,e):
        if(high==low):
            if l[low]==e:
                return True,low
            else:
                return False,-1
        mid=(low+high)//2
        if l[mid]==e:
            return True,mid
        elif l[mid]>e:
            if mid==low:
                return False
            else:
                return b(low,mid-1,l,e)
        else:
            if mid==high:
                return False
            else:
                return b(mid+1,high,l,e)
    length=len(l1)
    if length==0:
        return False
    else:
        return(b(0,length,l1,e))
print(l1)
print(best_bisec(l1,65))

     
    

