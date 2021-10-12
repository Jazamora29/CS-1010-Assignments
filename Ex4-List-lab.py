#Jose Andres Zamora
#make num list and print
num_list = [34, 42, 99, 1301, 1, 78, 314, 818, 777]

print(num_list)

print("----------------")
#I use -infinity as it is the lowest possible value, then make the count and iteration set to zero
maxint = float('-inf')
count = 0
i = 0
while i < len(num_list):
    count += 1#increase count for each iteration
    if num_list[i] > maxint:#if the current number is greater than the previous max, change the max to current number
        maxint = num_list[i]
    if i != len(num_list) - 1:#if we are not at the last number then add a ", "
        print(num_list[i], end=", ")
    else:#when we are at the end just pring the last nuber and go to next line
        print(num_list[i])
    i += 1#increase iteration num
print("Max value in this list is: " + str(maxint))#print the max and count
print("There are " + str(count) + " numbers in this list")