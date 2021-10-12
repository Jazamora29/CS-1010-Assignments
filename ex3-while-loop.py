#Jose Andres Zamora
#I have a while loop controlled by the boolean boo, also a count variable to store the count
boo = False
count = 0
while boo == False:
    x = input("Please enter a number to add or 'q' to quit: ")#grab user input for an integer, or the char q
    if(x != 'q'):#if it isn't 'q' we can assume it is an integer
        count += int(x)#add integer to the total
        print("Your subtotal is " + str(count))#print sub total
    else:
        print("Your grand total is " + str(count))#if we quit, then we print grand total
        print("Thank you")#thank the user