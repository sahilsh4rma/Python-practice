x=int(input("Enter a number : "))
guess=x/2
eclipse=0.01
while(abs((guess**2)-x)>eclipse):
    guess=guess-(((guess**2)-x)/(2*guess))
print(guess)