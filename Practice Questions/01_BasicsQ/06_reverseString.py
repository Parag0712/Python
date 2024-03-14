def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

original_string = "Hello, World!"
result = reverse_string(original_string)
print(result)
