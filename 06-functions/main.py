# Lets go over what a function is and how to use them
# A function is a block of code that is used to perform a specific task
# Lets create a function that prints a message to the console

def printMessage():
    print("Hello World")
    
# To call a function, use the function name followed by parenthesis
# printMessage()
# You can also pass data, known as parameters, into a function
# Lets create a function that prints a message to the console along with a name


def printMessage2(name):
    print("Hello " + name)

# To call a function, use the function name followed by parenthesis
# You can use functions within functions
# Lets create a function that prints a message to the console along with a name


def printMessage3(name):
    print("Hello " + name)
    printMessage()


printMessage3("Bunny buns bakery")

# Using functions within functions is called function nesting
