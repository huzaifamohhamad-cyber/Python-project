import random as rm

n=["sharuk khan","modi",
"salman khan",
"nirmala sitaraman",
"virat kilo",
"jp morgan",
"alok "
,"mukesh ambani"
]
a=["doing timepass",
"dancing with monkey",
"eating sugar with papa",
"talking with birds",
"sit with donkey",
"spoted",
"riding on  elephant",
"runnig behind the dog",
]
e=["at taj mahal",
"at goa beach",
"at the coffe shop",
"at local train",
"at taj hotel",
"at mohammad ali road ","at a zoo."]
while True:
   r1=rm.choice(n)
   r2=rm.choice(a)
   r3=rm.choice(e)
   print(f"Breaking News:\nOmg {r1} {r2} {r3}.")
   print("type yes if you want to continue otherwise type no:")
   i=input().strip().lower()
   if i=="no":
    break
