import random

n=random.randint(1,100)
a=0
guesses=1
while(a != n):
    a=(int(input("enter the number between 1 to 100:")))
    if(n>a):
        print("guess higher number.")
        guesses +=1
    elif(a>n):
        print('guess lower number.') 
        guesses +=1

print(f"you take {guesses} atempts to guess {n}")           