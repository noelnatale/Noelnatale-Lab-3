# this function adds two numbers
def add(x,y):
    print(x + y)
# this function subtracts two numbers
def sub(x,y):
    print(x - y)
# this function multiplies two numbers
def mul(x,y):
    print(x * y)
# this function divides two numbers
def div(x,y):
    print(x / y)

EASTER_EGG_NUMBER = 17
##############################################################################################
#start of program
print("welcome to the calculator")
print("what would you like to do?")
print("Type(a)dd (s)ubtract (m)ultiply (d)ivide (q)uit")

user_choice = input(": ")
#print(user_choice)

if user_choice == str(EASTER_EGG_NUMBER):
    print("Easter egg activated! 17 is my lucky birthday number!")
    raise SystemExit

if user_choice == 'a' :
    x = int(input("Enter the first number"))
    y = int(input("Enter the second number"))
    add(x,y)

#elif for subtract
if user_choice == 's' :
    x = int(input("Enter the first number"))
    y = int(input("Enter the second number"))
    sub(x,y)
##elif for multiply
if user_choice == 'm' :
    x = int(input("Enter the first number"))
    y = int(input("Enter the second number"))
    mul(x,y)
#elif for divide
if user_choice == 'd' :
    x = int(input("Enter the first number"))
    y = int(input("Enter the second number"))
    div(x,y)
#elif for quit
# break- this will not work without a loop

#else - does not need a contition!!!
#else:
#print invalid input

