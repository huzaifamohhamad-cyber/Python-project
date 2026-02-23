import random

computer=random.choice([-1,0,1])
you1=input("enter your choice:")
you2 = {"rock":-1,"paper":0,"scissor":1}
reversedict={-1:"rock",0:"paper",1:"scissor"}
you = you2[you1]
print(f"you chose {reversedict[you]},computer chose {reversedict[computer]}")
if (computer==you):
    print("its a draw")

else:
    if(computer==-1 and you==0):
        print("you win")

    elif(computer==-1 and you==1):
        print("you lose.")

    elif(computer==0 and you==1):
        print("you win") 

    elif(computer==1 and you==0):
        print("you lose .")

    elif(computer==0 and you==-1):
        print("you lose")  

    elif(computer==1 and you==-1):
        print("you win.")    

    else:
        print("something went wrong.")        
