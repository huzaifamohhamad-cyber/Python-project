import random as rn

print("welcome in the random guessing game.")
e_w=["apple","orange","train","car","bike","air","cat"]
m_w=["banana","monkey","bottle","laptop","airplane","mobile","huzaifa"]
h_w=["diamond","mountain","travel","elephant","umbrella","rainning"]
level1=input("enter the dificullty level:").strip().lower()
if level1=="easy":
    word=rn.choice(e_w)
elif level1=="mediam":
    word=rn.choice(m_w)
elif level1=="hard":
    word=rn.choice(h_w)

else:
    print("invalid input,set duficullty level ad mediam") 
    word=rn.choice(m_w)  

attempts=0
print("guess the secret word :")
 
while True:
    secret=input().lower()
    attempts +=1
    if word==secret:
        print(f"Congratulation.....  you chose correct word in {attempts}")
        break
    hint=""
    for  i in range(len(word)):
        if i<len(secret) and word[i]==secret[i]:
            hint+=secret[i]

        else:
            hint+="_"
    print(f"Hint:{hint}")            
print('game over...')    