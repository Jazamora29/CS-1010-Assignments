#Jose Andres Zamora
#make 3 variables and print them
p1 = "A Red Fox"
p2 = "chased a Blue Mouse"
p3 = "accross a meadow"

print(p1)
print(p2)
print(p3)

print("----------------")
#make a variable that combines the 3 already made, also add space inbetween them
story = p1 + " " + p2 + " " + p3

print(story)

print("----------------")
#use .lower() as I know this doesn't affect the string, just the returned string. Since this goes straight to the print I don't need to make a new variable
print(story.lower())
print(story)

print("----------------")
#same as above
print(story.upper())
print(story)

print("----------------")
#I get the char in the 19th index of the string
print(story[19])

print("----------------")
#I go from index 19 to 23 in order to get "Blue"
print(story[19:23])

print("----------------")
#print length
print(len(story))

print("----------------")
#check if the string is numeric
print(story.isnumeric())

print("----------------")
#make a string with just a number and check if it is numeric, which it is
num = "4"
print(num.isnumeric())