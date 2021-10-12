#Jose Andres Zamora
#create a variable to store the count and x to store the number we add by
count = 0
x = 1
while x <= 100:#create a while loop that continues when x <= 100
    print(str(count) + " + " + str(x) + " = " + str(count + x))#print the total + x in an equation to show the user what is happening
    count += x#increases count for the next iteration
    x += 1#increases x for the next iteration
print("done")#we are done, so we print "done"