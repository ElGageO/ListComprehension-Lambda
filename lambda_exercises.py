''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
from asyncio import format_helpers


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x % 2 == 0, nums))
odds = list(filter(lambda x: x % 2 == 1, nums))

print(evens)
print(odds)


''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

six_chars = list(filter(lambda day: len(day) == 6, weekdays))

print(six_chars)


''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''

colors = ['orange', 'red', 'green', 'blue', 'white', 'black']

new_colors = list(filter(lambda color: color not in ['orange', 'black'], colors))

print(new_colors)


''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

list3 = list(filter(lambda x: x not in list2, list1))

print(list3)


''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''

colors2 = ['red', 'black', 'white', 'green', 'orange']

new_colors2 = list(filter(lambda color: 'ack' in color, colors2))
print(new_colors2)


''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''

#password = input('Please enter a password: ')
password = 'Abcdefg1'
password_list = list(password)

verified_list = []
upper = False
lower = False
number = False
length = False
for char in password_list:
    if char.isupper():
        upper = True
    elif char.islower():
        lower = True
    elif char.isdigit():
        number = True
    
    if len(password_list) >= 8:
        length = True

verified_list.append(upper)
verified_list.append(lower)
verified_list.append(number)
verified_list.append(length)

verification = lambda x: all(x)
password_check = verification(verified_list)

if password_check:
    print('Password verified')
else:
    print('Password does not meet requirements')


''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''

