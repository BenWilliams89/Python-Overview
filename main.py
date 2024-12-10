""" this comments out any code
"""
"""variables"""
my_number = 5
print(my_number)

"""" function """

def multiplication(num1, num2):
    return num1 * num2

result1= multiplication(2,3)
print(result1)
""" returns 6 - 2 * 3 = 6

""" Determining data types """

numbers, boolean, set, sequence types & Dictionary (data mapping)
"""
""" print(type('hello)) """ prints class 'str' """ for string

""" print(type(42)) """ prints class int - number'

Print (type(3.145)) = float - number with decimals
print (type(1j)) prints complex - mix of objects
print (type([egg, bacon, spam])) prints list
print(type(egg,bacon,spam)) prints tuple
print(type({name : john, age : 80})) prints dict

print(isinstance(3.14, int)) = False = as 3.14 is not a integar it is a float

""" integers, floats and decimals """

integer = a whole number (3)
float = a number with a decimal (2.76)

int() float() complex()

None = 0

When receiving information like from a form on a website, the information comes through as a string
We use int() to convert it to a number
float() to convert it to a float

or to convert a int/float into a string we use str()

int()	Converts to an integer
float()	Converts to a floating-point number
hex()	Converts a number to a hexadecimal string
oct()	Converts a number to a octal string
tuple()	Converts to a tuple
set()	Converts to a set
list()	Converts to a list
dict()	Converts a tuple into a dictionary
str()	Converts a number into a string

first_number = input("input your first number") - 2
second_number = input("input your second number") -2 
print(first_number + second_number) = 22 as the input is a string
+ is concatination

to change the above to numbers we do:

first_number = int(input("input your first number")) - 2
second_number = int(input("input your second number")) - 2
print(first_number + second_number) = 4

my_number = str(5)
my_string "5"

print(my_string + my_number) = 55

result = 40 + float('2.2)
print (result) = 42.2

result_two = "hello + str(42)
print(result_two) = hello 42

""" in python division always returns a float""" decimal number - whatever the answe is

5**5 = the power of 5 = 5 * 5 * 5 * 5 * 5

modulo % = divides the first number by the second number and returns the remainder
eg 5 / 5 = 1 but 5 % 5 = 0 as there is no remainder

""" Python f-string function """
f'{string or expression}'

name = input('what is your name") - string
age = input('what is your age) - number
print (f'hello {name}, you are {age} years old) = adding f means we can print strings and numbers without needing to change them

name = 'Ben'
age = 35
print(f "{name} is {age}) = Ben is 35

""" types of string methods"""

capitalize()	Capitalizes the first character of the string
center()	Centers string
count()	Returns a count of times a specified value occurs in the string
encode()	Returns an encoded version of the string (use decode() to decode)
endswith()	Returns True if the string ends with a specified suffix
expandtabs()	Sets the tab size in spaces of the string
find()	Returns the lowest index position of where a specified character was found
index()	Searches for a specified value and returns the position of where it was found or an error if not found
isalnum()	Returns True if all characters are alphanumeric
isalpha()	Returns True if all characters are alphabetic
isdigit()	Returns True if all characters are digits
islower()	Returns True if all characters are lower case
isspace()	Returns True if all characters are whitespace
istitle()	Returns True if the string is titlecased
isupper()	Returns True if all characters in the string are upper case
join()	concatenates string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
partition()	Returns a tuple where the string is parted into two strings and the separator
replace()	Returns a string where a old value is replaced with a new value
rfind()	Searches highest index in the string for a specified value
rindex()	Same but with error if nothing found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into uppercase
zfill()	Fills the string with a specified number of 0 values at the beginning

""" Comparision Operaters """

== is equal too
> is greater than
< is less than
>= is greater then or equal to
<= is less than or greater to
!= is not equal to

true and true = true
true and false = false
true or flase = if any statement is true then true is returned with and = true
print(not(4 < 5 and 4 < 10)) = false as not is used

""" The In keyword"""

The in keyword is the same as includes 
in returns true or false
not in is the oppositite

print('Program' in 'Programming') = true
print('spam' in ['spam', 'egg']) = true
print('sausage' not in ['spam', 'egg']) = 

""" If & Else statements """

if number == 5: - uses : to run
    print(f"{number} is equal to 5")
else:
    print(f"{number} is not equal to 5")

    this can also be written as:
    a if c else b 
        = if a & c are equal otherwise do b

""" Buzz Fizz Game"""
num = 15

if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
elif num % 3 == 0:
    print('Fizz')
elif num % 5 == 0:
    print('Buzz')
else:
    print(num)

another example:

if number > 5:
    print(f"{number} is greater than 5")
elif number < 5:
    print(f"{number} is less than 5")
else:
    print(f"{number} is not greater than, or less than 5. Therefore, {number} must be equal to 5.")

another example:

day = 'Friday'

if day == 'Monday':
    print('Meeting at 9:00')
elif day == 'Wednesday':
    print('Meeting at 2:00')
elif day == 'Friday':
    print('Meeting at 4:00')
else:
    print('No meetings today')

""" Nested If & Else statement """

admin = True
update_required = True

if admin:
    if update_required:
        print("You are authorized to update")
    else:
        print("No update required")
else:
    print("You need admin privileges to do this")

""" For loops """

languages = ["HTML", "CSS", "JavaScript"]
for language in languages:
  print(language) = HTML, CSS & JavaScript are printed to the console

  for character in "python"
  print(character) = p y t h o n

  range() loops through a specific number of times
  range() - takes 3 agruments - start, stop, step

  len() - length

 
  foods = ['bacon', 'sausage', 'egg', 'spam']

for ind in range(len(foods)):
	# In this example only the index is iterated over not the value
    print(ind, foods[ind])
print(foods)
# In this case we need to calculate the length of the foods collection
# Then we generate a range of integers equal to that length
# Then we iterate over that range of integers

another example:

users = ['anna', 'chris', 'brian']
for ind in range(len(users)):
    users[ind] = users[ind].capitalize()

print(users) = [Anna, Chris, Brian]

""" While loops """

run a block of code indefinetly (if condition is true) - when false the code stops

countdown_number = 10

print("Initiating Countdown Sequence...")
print("Lift Off Will Commence In...")

while countdown_number >= 0:
    print(f"{countdown_number} seconds...")
    countdown_number -= 1  = -= reduces by one

print("And We Have Lift Off!") - countsdown to 0

another example:

play_game = True

while play_game:
    continue_playing = input("Would you like to continue playing the game? y/n ")
    
    if continue_playing.lower() == "y":
        print("You have decided to continue playing the game.")
    elif continue_playing.lower() == "n":
        print("Now closing the game...")
        play_game = False
    else:
        print("That is not a valid option. Please try again.")

print("Thanks for playing")

an example of counting up:

num = -1

while num <= 8 and num >= -2:
    num += 1
    print(num)

""" Break, Continue & Pass """

Break stops the code from executing:

for number in range(10):
    if number == 5:
        break    # break here

    print(f'Number is  {number}')

print('Left the loop')

continue skips ahead:

for number in range(10):
    if number == 5:
        continue    # continue here

    print(f'Number is  {number}')

print('Left the loop')


Pass is diregarded - more of a placeholder

for number in range(10):
    if number == 5:
        pass    # pass here

    print(f'Number is  {number}')

print('Left the loop')

Example of +1 and break:

x = 0
while x < 10:
    if x == 8:
        break
    print(x)
    x += 1

print(f"Loop exited with x={x}")

example of pass and +1:

x = 0
while x < 14:
    if x > 4 and x < 11:
        pass
    else:
        print(x)
    x += 1

""" Nested Iteration """

i = 2
while i < 10:
    j = 2
    while j <= i/j:
        if not i % j:
            break
        j += 1
    if j > i/j:
        print(f'{i} is a prime number')
    i += 1

    prints to the console = 2,3,5,7 is a prime number

    Another example:

    x = 0
while x <= 3:
    y = 200
    while y <= 203:
        print(x, y)
        y += 1
    x += 1


""" List rules """

fruits = ['apple', 'orange', 'banana', 'pear', 'plum']

# Print all fruits
for fruit in fruits:
    print(fruit)

print()

# Get an item located in a list
second_item = fruits[1]
print(second_item)
print()

# Add an item to the list
fruits.append('cherries')
print(fruits)
print()

# Reverse the list
fruits.reverse()
print(fruits)

# Sort the list alphabetically:
fruits.sort()
print(fruits)

example of pulling data from a list:

all_numbers = [1, 5, 44, 22, 13, 17, 56, 3, 88, 9, 97]
big_numbers = []
for number in all_numbers:
    if number > 40:
        big_numbers.append(number)

print(all_numbers)
print(big_numbers)

""" List Indexing"""

take an item from a list - known as elements
last item in the list has the index -1 - lists start at 0 index
mylist[-2] = takes the second to last item etc


example:

fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
# As lists are zero-indexed index 0 is the first element
print(fruits[0])
# Using an index of -1 gives the last element. Negative indexing counts from the right
print(fruits[-1])
print(fruits[2])

this prints apple, orange and peach

""" List slicing """

slice the list up
slice(2) - takes the first two items in a list
slice has 3 arguments = start, end & step

fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
x = slice(1, 4, 2) - 1 = start, 4 = stop, 2 = step (take the 2nd element between 1 and 4)
fruits[x]

this produces banana and pear - because 1 is the start (banana), it stops at plum(4) then takes the 2 element between them = (pear)

"""List notation"""

slice shorthand = [0:2] = 0 is start, 2 is stop
this takes everything up until the second element but does NOT include the second element

example of a slice with 2 arguments:

fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
print(fruits[0:2])

This prints apple and banana

example of a slice with 3 arguments:

fruits = ["apple", "banana", "peach", "pear", "plum", "orange"]
print(fruits[0:4:2])

This prints apple and peach

Another example:

names = ["Mark", "Betty", "John", "Sally", "Bill", "Steven", "Mary", "Emily", "Adam"]


name = names[2]
print(name) = John

two_names = names[2:4]
print(two_names) = John & Sally

other_names = names[1:6:2]
print(other_names) = Betty, Sally, Steven start at betty end at mary take the 2nd from between

""" List Methods"""


Method	Description
list.append(x)	Add an item to the end of the list.
list.extend(list)	Extend the list by appending another list.
list.insert(i, x)	Insert an item at a given position. The first argument is the index of the element before which to insert
list.remove(x)	Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
list.pop(i)	Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
list.clear()	Remove all items from the list.
list.index(x, start, end)	Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.The optional arguments start and end are interpreted as in the slice notation.
list.count(x)	Return the number of times x appears in the list.
list.sort(key=None, reverse=False)	Sort the items of the list in place
list.reverse()	Reverse the elements of the list in place.
list.copy()	Return a copy of the list. Equivalent to a[:].

Note that methods which alter the list (reverse, append and sort) return None when printed. print(menu.reverse()) prints none - print menu again to get result
Methods that do not return any value return None as default in Python. 
Other methods like count, index and pop return integers, indices and items respectively

example:

menu = ['eggs', 'bacon', 'spam', 'spam']
print(menu) = displays all
print(menu.count('spam')) = 2 as spam appears twice
print(menu.count('eggs')) = 1
print(menu.index('eggs')) = 0 as eggs is the first index
print(menu.reverse()) = none as reverse produces none
print(menu) = the menu in reverse
print(menu.append('lobster thermidor')) = produces none - same as reverse
print(menu) = adds these to the list and prints the whole list
print(menu.sort()) - produces none
print(menu) = prints menu in alphabetical order
print(menu.pop()) = prints spam as that is the last item on the list

Example:

crew = ["Jean-Luc", "Wesley", "Warf", "Deanna", "William", "Data", "Geordie", "Tasha"]
print(crew) = prints all names
crew.pop()
print(crew) = prints all expect Tasha
crew.append("Beverly")
print(crew) = adds Beverly to the end
crew.extend(["Miles", "Guinan"])
print(crew) = adds the two names above to the list
crew.sort(key=len, reverse=True) = sort by length of the string and reverse it as reverse is true
print(crew)

""" Tuples """
