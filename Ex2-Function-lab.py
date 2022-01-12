#Jose Andres Zamora
import random

def dice():#simple, just use randint function
    print(random.randint(1, 6))

def dice1():#instead of print we return
    return(random.randint(1,6))

def dice2(num):#take an integer input and set that as end point for randint
    return(random.randint(1, num))

def dice3(num = 6):#do the same as above, but have the default value set as 6
    return(random.randint(1, num))

def checkSides(num):#here we check if the int input is 4, 6, 8, 10, 12, or 20.
    if(num == 4 or num == 6 or num == 8 or num == 10 or num == 12 or num == 20):
        return True#if it is, we return true
    else:
        print("Integer must be 4, 6, 8, 10, 12, or 20. Default of 6 is used")
        return False#if not we tell the user that we will use 6 instead and return false
    
def dice4(num):
    if checkSides(num) == True:#checks if num is valid
        return(random.randint(1, num))#returns with input as valid if so
    else:
        return(random.randint(1, 6))#if not, we use 6

def dice5(num, rolls):#here we do the same but with a list
    x = []#create a list
    if checkSides(num) == True:
        while rolls > 0:#use while loop to repeat a certain amount of times
            x.append(random.randint(1, num))#add result to the list
            rolls -= 1#decrease rolls each iteration by 1
        return x
    else:#same as above but we use 6 as endpoint
        while rolls > 0:
            x.append(random.randint(1, 6))
            rolls -= 1
        return x
print("--- normal dice ---")
dice()
print("--- dice 1 ---")
print(dice1())
print("--- dice 2 (30) ---")
print(dice2(30))
print("--- dice 3 (100), (no input) ---")
print(dice3(100))
print(dice3())
print("--- dice 4 (20), (3) ---")
print(dice4(20))
print(dice4(3))
print("--- dice 5 (20, 10) (3, 20)")
print(dice5(20, 10))
print(dice5(3, 20))