from pickle import TRUE
import random

def gameWin(comp, you):
    # r-rock  p-paper  s-scissor
    #  comp-computer for random number generated
    if comp == you:
        return None
    elif comp=='p':
        if you=='r':
            return False
        elif you=='s':
            return True
    elif comp=='r':
        if you=='p':
            return True
        elif you=='s':
            return False
    elif comp=='s':
        if you=='p':
            return False
        elif you=='r':
            return True             


   
