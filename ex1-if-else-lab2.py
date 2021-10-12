import random
#creates a boolean for a loop to allow the user to play again
boo = False
while boo == False:
    #generates a random number from 0-2 to represent a computer choice, then asks for user input
    y = random.randint(0,2)
    x = input("Enter your choice of Rock(R), Paper(P), or Scissors(S)")
    #prints what the user inputed but in a way for the reader to understand
    if x == 'R':
        x = 0
        print("User selected Rock")
    elif x == 'P':
        x = 1
        print("User selected Paper")
    elif x == 'S':
        x = 2
        print("User selected Scisors")
    #prints what the computer selected in a way for the reader to understand
    if y == 0:
        print("Computer selected Rock")
    elif y == 1:
        print("Computer selected Paper")
    elif y == 2:
        print("Computer selected Scisors")
    #checks if user inputed valid inputs
    if ((x == 1) or (x == 2) or (x == 3)):
        #checks for tie
        if x == y:
            print("Tie")
        #checks for a user win
        elif (x == 0 and y == 2) or (x == 1 and y == 0) or (x == 2 and y == 1):
            print("User wins")
        #checks for a computer win, since tie and user win is already checked this is just else
        else:
            print("Computer wins")
    #if user input isn't accepted it lets them know
    else:
        print("invalid inputs")
    #makes a bool for a while loop
    boop = False
    #while loop to ask user if they want to play again
    while boop == False:
        z = input("Play again? Y/N ")
        #if no, changes Boop and boo to end the program and give the user a final message
        if(z == 'N'):
            boo = True
            boop = True
            input("Hope you had fun, press enter to quit")
        #if it is not a Y, aka a non valid input it lets the user know and lets them try again
        elif(z != 'Y'):
            print("you put a wrong input")
        #lastly, if the user selects Y we simply end this loop but allow the original to loop again
        else:
            boop = True