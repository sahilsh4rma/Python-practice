def isPalin(s):
    s=s.lower()
    if len(s)<=1:
        return True
    else:
        return s[0]==s[-1] and isPalin(s[1:-1])
x="levl"
print(isPalin(x))