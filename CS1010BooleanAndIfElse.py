#note, all booleans are in true or false when printed, but binary does the same thing

print("spanish" == "portuguese")#for ==, spanish isn't the same string as portuguese, so false
print("software" != "hardware")#for !=, software isn't the same string as hardware, so true
print(5 > 3)#for >, 5 is grearter than 3, so true
print(7 < 2)#for <, 7 is not less than 2, so false
print(4 >= 4)#for >=, 4 is not greater than for but is equal to 4, so true
print(3 <= 6)#for <=, 3 is less than 6 but not equal to 6, so true

print("---") 

print(1 or 0)#for OR, 1/true or 0/false is true as we have atleast 1 true
print(1 and 1)#for AND, 1/true and 1/true is true as both are true
print(1 ^ 1)#for XOR, 1/true and 1/true is false as we can only have 1 true
print(not 1)#for NOT, 1/true's opposite is 0/false, so we print false

print("---")

print((("spanish" == "portuguese") ^ ("software" != "hardware")) and ((5 > 3) or (not (4>=4))))#based on previous examples, (false XOR true) and (true or false) = true and true = true
print((7 < 2) or (6 <= 3))#much more simple, false or false = false

print("===")

x = int(input("Please enter an integer ")) #takes an input
if x > 42:#checks if input is higher and prints
    print("Your number is higher")
elif x < 42:#checks if input is lower and prints
    print("Your number is lower")
else:#for any other instance, aka input = 42, prints
    print("You entered 42")

print("===")

x = float(input("Please enter your grade as a decimal "))#takes an input
if 90 <= x <= 100:#checks if you have an A and prints
    print("You have an A")
elif 80 <= x < 90:#checks if you have a B and prints
    print("You have a B")
elif 70 <= x < 80:#checks if you have a C and prints
    print("You have a C")
elif 0 <= x < 70:#checks if you failed and prints
    print("You have a NC")
else:
    print("Lair!!!")#if you give a number out of the range [0,100] you are a liar as you can't have a grade like that

print("===")
#print the intro and menu
print("================================")
print("Welcome to JZ's burger shop")
print("================================")
print("Menu:")
print("1 - McStandard (1 patty)")
print("2 - McGordo (2 patties)")
print("3 - McChonk (3 patties)")
#create arrays, boolean and an integer to start a while loop and keep track of the number of iterations
boo = False
burgers = []
cheese = []
combo = []
size = []
i = 0
while boo == False:
    #add burger order number to a burgers array; check if the input is valid
    burgers.append(int(input("Please select Burger [1,2,3] ")))
    if ((burgers[i] == 1) or (burgers[i] == 2) or (burgers[i] == 3)) == False:
        quit("Error " + str(burgers[i]) + " is not a valid input for burgers" )
    #add cheese input to cheese array; check if the input is valid
    cheese.append(input("Add cheese to your burger? [Y,N] "))
    if ((cheese[i] == "Y") or (cheese[i] == "N")) == False:
        quit("Error " + str(cheese[i]) + " is not a valid input for cheese")
    #add combo input to combo array; check if the input is valid
    combo.append(input("Would you like a combo? [Y.N] "))
    if ((combo[i] == "Y") or (combo[i] == "N")) == False:
        quit("Error " + str(combo[i]) + " is not a valid input for combo")
    elif combo[i] == "Y":
        #if wee do have a combo we add combo size to size array; check for valid input
        size.append(input("What Size? [M, L] "))
        if ((size[i] == "M") or (size[i] == "L")) == False:
            quit("Error " + str(size[i]) + " is not a valid input for size")
    #if we do not have a combo then we add null to the array as a filler for that space. Since there is no combo, in the future we won't need to check the size so null won't matter
    elif combo[i] == "N":
        size.append("null")
    #now we check if the customer wants to add another order, if not then we finish this loop. Also check if the input is valid
    b = input("Done? [Y, N] ")
    if b == "Y":
        boo = True
        print("--------------------------------")
        print("Your order")
        print("--------------------------------")
    elif b != "N":
        quit("Error " + b + " is not a valid input")
    #increase iteration number
    i += 1
#we set i back to zero and create a float variable price to keep track of the price
i = 0
price = 0.0

while i < len(burgers):
    #we check the burger array and print the burger they ordered along with price, then we add price to total
    if burgers[i] == 1:
        print("McStandard          $3.45")
        price += 3.45
    elif burgers[i] == 2:
        print("McGordo             $5.24")
        price += 5.24
    elif burgers[i] == 3:
        print("McChonk             $6.95")
        price += 6.95
    #we check the cheese array and print if they ordered cheese, then we add price if needed
    if cheese[i] == "Y":
        print("    With cheese        $1.23")
        price += 1.23
    #we check the size array. We know if size is L or M and not null then the customer ordered a combo. In either case we just print the size of their combo and the price
    if size[i] == "L":
        print("    Large combo        $3.89")
        price += 3.89
    elif size[i] == "M":
        print("    Medium combo       $2.76")
    #increase iteration number
    i += 1

#print the prices and tax and thank the customer
print("--------------------------------")
print("    Subtotal        " + str("{:0.2f}".format(price)))
print("    Tax             " + str("{:0.2f}".format(.095*price)))
print("--------------------------------")
print("    Total due       " + str("{:0.2f}".format(price + .095*price)))
print("================================")
print("Thank You!")