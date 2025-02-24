"""
Advanced Decorators
Create a logging_decorator() which is going to print the name of the function that was called,
the arguments it was given and finally the returned output:

1| You called a_function(1,2,3)
2| It returned: 6
The value 6 is the return value of the function.



Don't change the body of a_function.



IMPORTANT: You only need to use *args, you can ignore **kwargs in this exercise.
"""


# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        print(f"You called a_function{args}: " + str(function(*args)))
    return wrapper


#  Use the decorator 👇

@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)