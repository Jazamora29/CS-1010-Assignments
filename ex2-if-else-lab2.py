#sets up a while loop so user can play again
boo = False
while boo == False:
    #asks user a question, to pick an animal
    print("Choose between a Fish, Tarantula, Snake and Octopus")
    #seperates groups into two, then two again and from there you are left with answer
    #also prints the conclusion it reached
    #and lastly, inclused a few else statements to catch wrong inputs
    x = input("Does the animal have legs/arms? Y/N ")
    if x == 'Y':
        x = input("Does the animal primarily live in the water? Y/N")
        if x == 'Y':
            print("The animal is Octopus")
        elif x == 'N':
            print("The animal is Tarantula")
        else:
            print("Input Error, wrong letter")
    elif x == 'N':
        x = input("Does the animal primarily live in the water? Y/N")
        if x == 'Y':
            print("The animal is Fish")
        elif x == 'N':
            print("The animal is snake")
        else:
            print("Input Error, wrong letter")
    else:
        print("Input Error, wrong letter")
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