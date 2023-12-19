#Efficient way to do Fibnoacci Series
def fib(n,d):
    if n in d:
        return d[n]
    else:
        ans=fib(n-1,d)+fib(n-2,d)
        d[n]=ans
        return ans
d={1:1,2:2}
x=3
print(fib(x,d))