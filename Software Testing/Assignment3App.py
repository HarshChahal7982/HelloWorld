import Assignment3engine
from pickle import TRUE
import random

print("computer turn: rock(r) paper(p) or scissor(s)?")
randNo=random.randint(1,3)


if randNo == 1: 
    comp='r'
elif randNo == 2:
    comp='p'
elif randNo == 3:
    comp='s'

you=input("Player's turn: rock(1) paper(2) or scissor(3)")
a=Assignment3engine.gameWin(comp,you)

print(f"computer choose {comp}")
print(f"you choose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("you win!")
else:
    print("you lose!") 