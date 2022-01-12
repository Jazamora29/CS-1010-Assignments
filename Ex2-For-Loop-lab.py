#Jose Andres Zamora

my_list = ['earth', 'exciting', 'day', 'laptop', 'electrochemical', 'blue', 'up']
#make variables to store the longest string and it's length
max = 0
stor = ""
for x in my_list:
    print(x + " " + str(len(x)))#print the word and then its length
    if(max < len(x)):#check if the current word it longer, then replaces the storage variables if they are
        max = len(x)
        stor = x
print("Longest word is " + stor)#print longest word

print("----------------")

my_list = ['indistinguishable', 'acorn', 'soap', 'ladder', 'cheese', 'disillusioned', 'pit', 'monday', 'placeholder', 'teleconference']

max = 0
stor = ""
for x in my_list:
    print(x + " " + str(len(x)))
    if(max < len(x)):
        max = len(x)
        stor = x
print("Longest word is " + stor)

print("----------------")

my_list = ['fixture', 'dangerous', 'humanitarianism', 'trip', 'orange', 'cat', 'triskaidekaphobia', 'nominal', 'and', 'atomic']

max = 0
stor = ""
for x in my_list:
    print(x + " " + str(len(x)))
    if(max < len(x)):
        max = len(x)
        stor = x
print("Longest word is " + stor)