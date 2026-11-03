import random

def roll():
    return random.randint(1,6)

def pigTurn():
    turnTotal = 0
    rolledOne = False
    while turnTotal < 20 and not rolledOne:
        dice =  roll()
        print("Roll:", dice)
        if dice == 1:
            turnTotal = 0
            rolledOne = True
        else:
            turnTotal += dice
    print("Turn total:", turnTotal)

print(pigTurn())
