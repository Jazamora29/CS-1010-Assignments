#sets up a while loop so user can play again
boo = False
while boo == False:
    #asks user a question, to pick a shape
    print("Choose between the shapes")
    #seperates groups into two, then two again and so on and from there you are left with answer
    #also prints the conclusion it reached
    #and lastly, inclused a few else statements to catch wrong inputs
    x = input("Does the shape have an outline? Y/N ")
    if x == 'Y':
        x = input("is the shape red? Y/N")
        if x == 'Y':
            x = input("Is there 3 sides? Y/N")
            if x == 'Y':
                print("You selected 5")
            elif x == 'N':
                print("You selected 7")
            else:
                print("Input Error, wrong letter")
        elif x == 'N':
            x = input("Is there 4 sides? Y/N")
            if x == 'Y':
                print("You selected 6")
            elif x == 'N':
                print("You selected 8")
            else:
                print("Input Error, wrong letter")
        else:
            print("Input Error, wrong letter")
    elif x == 'N':
        x = input("is the shape red? Y/N")
        if x == 'Y':
            x = input("Is there 4 sides? Y/N")
            if x == 'Y':
                print("You selected 2")
            elif x == 'N':
                print("You selected 4")
            else:
                print("Input Error, wrong letter")
        elif x == 'N':
            x = input("Is there 3 sides? Y/N")
            if x == 'Y':
                print("You selected 1")
            elif x == 'N':
                print("You selected 3")
            else:
                print("Input Error, wrong letter")
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