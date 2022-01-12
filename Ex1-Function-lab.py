#Jose Andres Zamora

def printHello():#pretty simple, just print the string
    print("hello from my function")

def print1to20():#here we can use the range from last week and then a for loop to print the the numbers from 1 to 20
    nums = range(1, 21)
    for x in nums:
        if x != nums[0]:#for any number past the first we add a comma in front
            print(", " + str(x), end="")
        else:#for first number we don't print comma
            print(x, end="")
    print()

def times7(num):#simple, print num*7
    print(num*7)

def sortString(words):#use .sort() to sort string and then print
    words.sort()
    print(words)

printHello()
print("-------------")
print1to20()
print("-------------")
print("4 times 7 is ", end="")
times7(4)
print("7 times 7 is ", end="")
times7(7)
print("-------------")
print("Hello, my, name, is, Jose")
sortString(["Hello", "My", "Name", "Is", "Jose"])