#Jose Andres Zamora

my_list = [4, 76, 2, 234, 9, 71]

print("input list is: ", end="")
#make storage variables to store sum and the max value
sum = 0
max = 0
for x in my_list:
    sum += x#increase sum
    if max < x:#check if the current value is larger than stored max, then replace if so
        max = x
    if x == my_list[0]:#if we are at the beggining we just pring the first number
        print(x, end="")
    else:
        print(", " + str(x), end="")#afterwards we pring the numbers but with a comma to seperate them
print()#new line
print("sum = " + str(sum))#print the sum
print("average = " + str(sum/len(my_list)))#print the average, sum/#
print("largest number = " + str(max))#prints the largest number

print("-------")

my_list = [3, -17, 99, -32, 321, 62, 27]

print("input list is: ", end="")
sum = 0
max = 0
for x in my_list:
    sum += x
    if max < x:
        max = x
    if x == my_list[0]:
        print(x, end="")
    else:
        print(", " + str(x), end="")
print()
print("sum = " + str(sum))
print("average = " + str(sum/len(my_list)))
print("largest number = " + str(max))

print("-------")

my_list = [1899, 1978, 23, 0, 23, 37, 237, 8, 2, -77, 31]

print("input list is: ", end="")
sum = 0
max = 0
for x in my_list:
    sum += x
    if max < x:
        max = x
    if x == my_list[0]:
        print(x, end="")
    else:
        print(", " + str(x), end="")
print()
print("sum = " + str(sum))
print("average = " + str(sum/len(my_list)))
print("largest number = " + str(max))
