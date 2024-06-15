"""
Recursion - a function that calls itself... until it doesn't.
Base case - a case when the function will stop calling itself; it must have a return statement.
Recursive case - when the function needs to call itself again; If we only have a recursive case, we will get a Stack Overflow

# Call Stack
Call Stack - The call stack is how Python remembers where to return the execution after each function call. 
The call stack isn’t stored in a variable in your program; rather, Python handles it behind the scenes.
When your program calls a function, Python creates a frame object on the top of the call stack. 
Frame objects store the line number of the original function call so that Python can remember where to return.
If another function call is made, Python puts another frame object on the call stack above the other one.

Factorial - factorail(4), what happens after we return 1?
1. Draw the call stack down. IMAGE
2. Diagram out the path of the answer. 


"""


# Factorial Exercise my implementation
def get_factorial(number: int):
    "assumes number > 0"
    if number == 1:
        return 1
    return get_factorial(number - 1) * number


# course func
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(3))
