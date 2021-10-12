#Jose Andres Zamora
#make list of nums and print 4th number
my_num_list = [3, 6, 4, 83, 2, 7, 2, 17, 4, 9, 0, 44, 2]

print(my_num_list[3])

print("----------------")
#add 8 at the end and print
my_num_list.append(8)

print(my_num_list)

print("----------------")
#insert 33 after the 4th number, 83
my_num_list.insert(4, 33)

print(my_num_list)

print("----------------")
#use a for loop to count the number of 2s
count = 0
for x in my_num_list:
    if x == 2:
        count += 1

print("there are " + str(count) + " 2's in this list")

print("----------------")
#print length
print(len(my_num_list))

print("----------------")
#use a while loop and a storage list to remove the last for values and print them with the storage list
i = 0
stor = []
while i < 4:
    stor.append(my_num_list.pop())#remove and add to new list in the same line
    i += 1

print(len(my_num_list))

print("----------------")
#use while loop to print the list
i = 0
while i < len(my_num_list):
    print(my_num_list[i])
    i += 1