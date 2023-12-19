#string.spliT() use
s="hello hi there"
inte="1,2,3,4,5,6"
x=s.split()
y=inte.split(",")
print(x[1]," ",x," ",len(x),y)
# list(string): this will conver the string in list and every char its elements (even spaces)
l1=list(s)
print(l1) 
#
#''.join(list_name) use
s=["Sahil sharma","Sahil_Sharma"]
x="_".join(s)
print(x)