#Jose Andres Zamora
#make x = 1 and a while loop for when x <= 5
x = 1
while x <= 5:
    print("#" * x)#print triangle
    x += 1#increase x for each iteration

print("------------------")
#make x = 1 and y as the user input. The while loop is for when x <= y
x = 1
y = int(input("Select an Integer: "))
while x <= y:
    z = 0#make z in order for a second while loop when z < x
    while z < x:
        print("@", end="")#print '@' for z iterations
        z += 1#increase z to repeat x times
    print("")#next line
    x += 1#increase x to repeat y times
