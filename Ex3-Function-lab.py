#Jose Andres Zamora
import random
#check EX 2 for comments
def checkSides(num = 6):
    if(num == 4 or num == 6 or num == 8 or num == 10 or num == 12 or num == 20):
        return True
    else:
        print("Integer must be 4, 6, 8, 10, 12, or 20. Default of 6 is used")
        return False
#check EX 2 for comments
def dice5(num, rolls):
    x = []
    if checkSides(num) == True:
        while rolls > 0:
            x.append(random.randint(1, num))
            rolls -= 1
        return x
    else:
        while rolls > 0:
            x.append(random.randint(1, 6))
            rolls -= 1
        return x
#create variables and their starting values
boo = False
cycle = 'n'
num = 0
sides = 0
while boo == False:
    if cycle == 'n':#go here to set parameters
        num = int(input("Enter the number of dice to roll: "))#ask for input for endpoint
        sides = int(input("Enter the numver of sides the dice will have: "))#ask for the input for the number of sides
        print("-----------------------")#roll
        print(dice5(sides, num))
        print("-----------------------")
        cycle = input("Press Enter to re-roll, q to quit, or n to set new parameters: ")#ask if we want to repeat, quit or change parameters
    elif cycle == 'q':#go here to quit
        boo = True
    else:#go here if we just repeat
        print("-----------------------")#roll
        print(dice5(sides, num))
        print("-----------------------")
        cycle = input("Press Enter to re-roll, q to quit, or n to set new parameters: ")#ask if we want to repeat, quit, or change parameters
    
    