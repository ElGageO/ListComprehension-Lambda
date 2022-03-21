# Numbers 1-9
x = [ i for i in range(10) ]
print(x)

# Adding an expression: square of each number
squares = [ i ** 2 for i in range(10) ]
print(squares)

# Multiply each element by 3
list1 = [3, 4, 5]
multiplied = [ item * 3 for item in list1 ]
print(multiplied)

# First letter of each word in a list
list_of_words = ['this', 'is', 'a', 'list', 'of', 'words']
first_letter = [ word[0] for word in list_of_words ]
print(first_letter)

# Change upper case letters to lower case
upper_case = ['A', 'B', 'C']
lower_case = [ letter.lower() for letter in upper_case ]

# Adding an if condition: square of only even numbers from 0 - 4
new_range = [ i * i for i in range(5) if i % 2 == 0 ]
print(new_range)

# Separate numbers and letters within a string
string = 'Hello 12345 World'
nums = [ x for x in string if x.isdigit() ]
letters = [ x for x in string if x.isalpha() ]
print(nums, letters)

# Using a file
myfile = open('test.txt', 'r')
result = [ i.rstrip('\n') for i in myfile if 'line3' in i ]
print(result)

# Using functions
def double(x):
    return x * 2

mynumbers = [ double(x) for x in range(10)]
print(mynumbers)

# For even numbers only
mynumbers2 = [ double(x) for x in range(10) if x % 2]
print(mynumbers2)

# Adding more than one argument
result = [ x + y for x in [10, 30, 50] for y in [20, 40, 60]] # Behaves like a nested for loop, creates a list with 9 elements
print(result)
