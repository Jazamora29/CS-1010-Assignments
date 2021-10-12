#Jose Andres Zamora
import time
import random
#pretty simple, print, time.sleep(seconds), and repeat
print("Hello")
time.sleep(0.25)
print("I")
time.sleep(0.5)
print("am")
time.sleep(0.75)
print("very")
time.sleep(1.0)
print("sleepy")

print("----------------")
#Here we pring the time, wait half a second, print, 1 second then print
print(time.time())
time.sleep(.5)
print(time.time())
time.sleep(1.0)
print(time.time())

print("----------------")
#Here I have x = 1 and then a while loop that continues when x <= 10
x = 1
while x <= 10:
    print(x)#print the number
    x += 1#increase x by 1 each iteration, so we repeat 10 times as desired

print("----------------")
#Here I have x = 1 and then a while loop that continues when x  <= 10
x = 1
while x <= 10:
    #an if to check if x is 10. if x is 10 we know it's the end and I don't want there to be a " - " at the end
    if x != 10:
        print(x, end=" - ")#print the number and " - " so we don't move to the next line
    else:
        print(x)#when at the end simply print x
    x += 1 # increase x by 1 each iteration, so we repeat 10 times as desired

print("----------------")
#here I have x =  1 and ten a while loop that continues when x <= 5
x = 1
while x <= 5:
    print(x)#print x
    time.sleep(.5)#wait half a second
    x += 1#increase x by one each iteration so we repeat 5 times as desired

print("----------------")
#here I have x = 10 and a while loop that continues when x <= 20
x = 10
while x <= 20:
    #an if to make sure we aren't at the last iteration
    if x != 20:
        print(x, end=",")#print x and a comma, making sure not to move to the next line
    else:
        print(x)#print x as we are at the end and dont want to finish with a comma
    x += 2#increase x by 2 each itteration

print("----------------")
#here I have x = 20 and a while loop that continues when x >= 0
x = 20
while x >= 0:
    #we check if we are at the end
    if x != 2:
        print(x, end=",")#print x followed by a comma and make sure we don't move to the next line
    else:
        print(x)#print x as we are at the end and don't want to end with a ,
    x -= 3#decrease x by 3 as we were told to do

print("----------------")
#we have x = 10 and a while loop that continues when x >= 1
x = 10
while x >= 1:
    if x != 1:#check if we are at the end or not
        print(random.randint(0,100), end=" ")#if not, we print a random integer and add a space
    else:
        print(random.randint(0,100))#if we are, we pring a random integer and no space
    x -= 1#decrease x by 1 each iteration 

print("----------------")
#we have a while loop that continues while x <= 100
while x <= 100:
    x = int(input("Enter an integer greater than 100: "))#get user input
print("Thank you!")#if they enter an integer greater than 100 we exit the loop and end up here, printing "Thank you!"
