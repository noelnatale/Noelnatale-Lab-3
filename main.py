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

##############################################################################################
print("welcome to the calculator")
print("what would you like to do?")
print("Type(a)dd (s)ubtract (m)ultiply (d)ivide (q)uit")

x = int(input("Enter your first number:"))
y = int(input("Enter your second number:"))
add(x,y)
sub(x,y)
mul(x,y)
div(x,y)