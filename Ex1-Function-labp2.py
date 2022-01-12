#Jose Andres Zamora
def printHello():
    print("hello from my function")#prints out string into terminal

printHello()#call previous function

print("-------------")

def oneToTwenty():
    x = 1
    while(x < 21):
        print(x)
        x += 1

oneToTwenty()

print("-------------")

def timesSeven(num):
    print(num*7)

timesSeven(5)#calling function, should be 35
timesSeven(7)#calling function, should be 49

print("-------------")

def sortString(words):#use .sort() to sort string and then print
    words.sort()
    print(words)


sortString(["This","is","some", "code"])#calling function, code, is, some, this
