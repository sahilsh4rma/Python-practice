x=int(input("Enter the number: "))
if x<0:
    isNeg=True
    x=abs(x)
else:
    isNeg=False
y=''
while(x>0):
    y=str(x%2)+y
    x=x//2
if isNeg:
    y='-'+y
print(y)
