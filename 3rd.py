x=int(input("enter the number: "))
min=0
max=x
while(max>min):
    mid=(min+max)/2
    if abs(mid**2-x)<=0.01:
        break
    elif mid**2>x:
        max=mid
    else:
        min=mid
print(mid)