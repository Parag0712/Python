# how we handle Exception in python
# Python Try Except

# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

# These exceptions can be handled using the try statement:

# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
    a = 10/0
    print(a)
except Exception as e:
    print(f"Error: Division by zero is not allowed. {e}")
except ZeroDivisionError:
    print("other Exception")
finally:
    print("Hello ")