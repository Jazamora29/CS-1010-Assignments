#Jose Andres Zamora

listen = range(1, 6)#uses range to print a different number of 'o' for each line
for x in listen:
    print('o' * x)

print("----------------")

listen = range(6, 0, -1)#opposite of above, to do this we switch the boundries and then move down by 1
for x in listen:
    print('o' * x)

print("----------------")

count = int(input("enter an integer: "))#user input is stored
listen = range(1, count)#creates 1 range to count up
listen2 = range(count, 0, -1)#creates second deck to count down, along with the middle part
for x in listen:#print like previously, but with first range
    print('o' * x)
for x in listen2:#print like previously, but with second range
    print('o' * x)

print("----------------")

count = int(input("enter an integer: "))#takes user input
listeno = range(1, count + 1)#creates a range, count + 1 in order to become inclusive of count
for x in listeno:
    print(" " * (count - x), end="")#print the a number of spaces, I did some math
    print('o' * (-1 + 2*x))#print the desired numbers of 'o', I also did some math, pretty simple.