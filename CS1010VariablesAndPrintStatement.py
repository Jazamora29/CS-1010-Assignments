wombat = 15 #creates a variable "wombat" and assigns the int 15 to that variable
print("the value of wombat is") #prints desired string
print(str(wombat)) #prints the next desired string

horse = 37 #creates a new variable horse and assigns the int 37 to that variable
print(str(horse) + " is the value of horse") #prints desired string, uses str() to convert horse into a string in order for this to work

print(wombat + horse) #since we are using ints and no string we just need to add the variables and print
wombat = 27 
horse = -9 
#change values of the variables
print(wombat + horse) #add the variables again


print("===")


myString = "Hello there "
yourString = "Cal State LA"
#gives both variables the desired string
print(myString + yourString)#since both of the strings are the same type I just needed to use the + sign to add them

print("---")

a = 18
b = 17
c = a + b
#assign the desired values to the variables, then adds them to make c
print(c)#prints the variable c


print("===")


price = 6.95
taxRate = 7.25 * .01
tax = 0
tax = price * taxRate
#assign the desired values to the variables, then calculates the tax
print("the tax is " + "{:.2f}".format(tax)) #prints the desired string, uses str() to convert the variable tax into a string
#I was also curious and googled how to limit the number of decimal places, so I used "{:.2f}".format()

print("===")


x = int(input("Please input an iteger: "))#asks for the user to input an integer, and just ensures it isn't a float with the int()
print("the number you entered is: " + str(x))#prints desired string, using str() in order to make the input a string
print("your number in binary is: " + str(bin(x)))#does the same as above but uses bin() to make the integer binary
print("your number in hexadecimal is: " + str(hex(x)))#does the same, but uses hex() to make the integer into a hex number

print("Done")#just to separate current runs from previous runs
