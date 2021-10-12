import random
#sets up a while loop
boo = True
while boo == True:
    #asks the user to select their number of guesses
    i = int(input("How many guesses would you like? (Integers only)"))
    #stores the max range, and also generates the secret number
    rangeMax = 4*i
    secret = random.randint(0, rangeMax)
    #uses i>-1 to correctly run the number of itterations the user asked
    #also plays the game using ifs and elses to tell the user their guess' location to the secret number
    #and lastly, reminds them how many guesses are left
    while i > -1:
        y = int(input("The computer has generated a number from 0 to " + str(rangeMax) + ", guess the integer"))
        if y > secret:
            print("Number is smaller than your guess, you have " + str(i) + " guesses left")
        elif y < secret:
            print("Number is larger than your guess, you have " + str(i) + " guesses left")
        else:
            print("You Win!")
            i = 0
        i -= 1
    boop = False
    #while loop to ask user if they want to play again
    while boop == False:
        z = input("Play again? Y/N ")
        #if no, changes Boop and boo to end the program and give the user a final message
        if(z == 'N'):
            boo = False
            boop = True
            input("Hope you had fun, press enter to quit")
        #if it is not a Y, aka a non valid input it lets the user know and lets them try again
        elif(z != 'Y'):
            print("you put a wrong input")
        #lastly, if the user selects Y we simply end this loop but allow the original to loop again
        else:
            boop = True