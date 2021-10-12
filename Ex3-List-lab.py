#Jose Andres Zamora
#make a lsit of char and print
my_char_list = ['a', 'b', 'a', 'c', 'd', 'a', 'd', 'z', 'r', 'a']

print(len(my_char_list))

print("----------------")
#use .index to find the first d
print("d is at " + str(my_char_list.index('d')))

print("----------------")
#find the first c and go to the right 1 to add a
my_char_list.insert(my_char_list.index('c') + 1, 'a')

print(my_char_list)

print("----------------")
#print length
print(len(my_char_list))

print("----------------")
#count the number of a's
count = 0
for x in my_char_list:
    if x == 'a':
        count += 1
print("there are " + str(count) + " a's in the list")

print("----------------")
#print list
i = 0
while i < len(my_char_list):
    print(my_char_list[i])
    i += 1