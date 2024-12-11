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

tupes are not changeable - a collection of items similar to a list but collects data
creating a tuple is refered to as packing
a string with a comma after = a singleton tuple - ie "hello",

empty = ()
singleton = 'hello',
tup = 12345, 54321, 'hello!' # packing two ints and a string in a tuple
print(empty) = ()
print(singleton) = hello
print(tup)
print(tup[1])
x, y, z = tup # unpacking tuple into variables
print(z)


Example

cars = "Tesla", 'BMW', 'Ferrari',
print(cars)
get_car = cars[1]
print(get_car) = BMW
car_one, car_two, car_three = cars
print(cars[0])
print(cars[1])
print(cars[2])

"""Dictionaries"""

a way to store data
key: value pairs - like methods in JS

example of using a sictionary are mapping a phone number to a name

user = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

print(user)
print(user['age'])
user['home'] = 'Withywindle, Middle-Earth'
user['age'] = 99
print(user)
del user['home'] 
print(user)
print(list(user)) - prints username, first&lastname and age
print(sorted(user)) = sorts
print(user)
print('username' in user) = True

""" Getting & Setting Dictionary Items"""

dict() - creates dictionsaries from lists

keys = ['username', 'first_name', 'last_name', 'age']
default_value = ''
user = dict.fromkeys(keys, default_value)
print(user)
user['username'] = 'tombombadil'
user['first_name'] = 'Tom'
user['last_name'] = 'Bombadil'
user['age'] = 100
print(user)
print(user['age'])
print(user.get('home', "doesn't exist"))     - The .get stops an error if key is not set and sets status to 'deoesn't exist'
user['home'] = 'Withywindle, Middle-Earth'
user['age'] = 99
print(user)
del user['home'] 
print(user)
print(list(user.keys()))
print(list(user.values()))
print(user)

Example:

data = {
    "first_name": "Arthur",
    "last_name": "Dent",
    "species": "Human"
}

name = data['first_name']
print(name) = Arthur

species = data['species']
print(species) = Human

print(data.get('age', "Doesn't exist")) - creates age without throwing an error
data['age'] = 42 - sets age value to 42

print(data) prints all including age

""" Dictionary Methods """

clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a new dictionary with the specified keys and value
get(keyname, value)	Returns the value of the specified keyname. Used in the previous unit. Returns default None if the keyname doesn't exist unless you override this default with a optional value.
items()	Returns a list containing a tuple for each key:value pair
keys()	Returns a list containing the dictionary's keys. Used in the previous unit.
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key:value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key:value pairs
values()	Returns a list of all the values in the dictionary. Used in the previous unit.

user = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

print(user)
print(user.items())
print(user.get('age', 0))
user.update({'home': 'Withywindle, Middle-Earth'})
print(user)
print(user.popitem())
print(user)
user.clear()
print(user)

Another Example:

challenger = {
	"name": "Katniss Everdeen",
	"age": 16,
	"district": 12,
	"weapon": "Bow and Arrow", 
	"status": "Victor"
}

challenger.update({'occupation': 'Hunter'}) - adds hunter as an occupation

occupation = challenger.get('occupation')
print(occupation)

challenger.update({'age':17,}) - changes age to 17

challenger.pop('status') - removes status
print(challenger)

""" Sets """

python data type - mathmatical concept of items with no duplicates - good way to forbit duplicates
use case to to return unique words in a document
You can't change items in a set
add single items by using add() - multiple items with update() & discard() removes an item

breakfast = {'bacon', 'egg', 'spam', 'spam', 'spam', 'spam', 'spam'}
print(breakfast)
print('egg' in breakfast)
breakfast.add('sausage')
print(breakfast)
breakfast.update(['Lobster Thermidor', 'truffle pate', 'crevettes', 'shallots','aubergines'])
print(breakfast)
breakfast.discard('aubergines')
print(breakfast)

Sets have mathematic operations - union, intersection, difference and symmetric difference
union = all values that are one = | symbol
intersection = values in both sets = & symbol
differnece = value in first set and not the second set = - symbol
symmetric difference = all values in one set but not both = ^ symbol

Example:

hello = set("Hello")
world = set("World")
print(f"The unique letters in hello are: {hello}") = h , e, l, o
print(f"The letters in hello or world or both are: {hello|world}") = | is the symbol for union = h, d, l, w, r, e, o
print(f"The letters in both hello and world are: {hello&world}") = & is the symbol for intersection = l, o
print(f"The letters in hello but not world are: {hello-world}") = - is the symbol for difference = e, h
print(f"The letters in hello and world but not both are: {hello^world}") = ^ is the symbol for symmetric difference = r, e, h, d, w

Example:

product_list = ['hammer', 'saw', 'nails', 'wood', 'screws', 'paint', 'brushes', 'light bulbs']
products_bought = {'nails', 'screws', 'hammer', 'wood', 'saw', 'hammer', 'saw', 'nails', 'nails', 'screws', 'hammer'}

products_bought.add('light bulbs')
products_bought.update(['wood', 'screws', 'saw'])

has_nails = 'nails' in products_bought
has_paint = "paint" in products_bought
unsold_items = set(product_list) - products_bought   = Set converts to a set from a list

print(has_nails)
print(has_paint)
print(unsold_items)

""" Iterating Python Data Structures """

If we needed access to both keys and values, we’d have to use a dictionary method called .items()

user = {
    "username": "tombombadil",
    "first_name": "Tom",
    "last_name": "Bombadil",
    "age": 100
}

for key, value in user.items():
    print(f"Key: {key}")
    print(f"Value: {value}")
    print("------------------")

    prints = key: username, value: tombombadil, ---

    Example:

    data = {
	"first_name": "brian",
	"last_name": "johnson",
	"occupation": "student"
}

for key, value in data.items():
    print(f"{key}:{value}") - This prints each key and value

for key, value in data.items():
    if value != 'student':
        data[key] = value.capitalize()
print(data)

this runs an if statement saying that update the strings that don't equal student to capitalise

example:

scores = [6, 9, 8, 7, 8, 9]

for ind in range(len(scores)):
	scores[ind] += 1

print(scores)

range(len(scores)) generates a sequence of indices from 0 to the length of the list minus one.

scores[i] += 1 increments the value at each index by 1.

""" List Comprehensions"""

A concise way to create a list

examples of how to create lists:

letters = [letter for letter in 'Marvin']
print(letters) = [m,a,r,v,i,n]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [number for number in numbers if number % 2 == 0]
print(evens) = [2,4,6,8,10]

""" Dictionary comprehensions"""

A concise way to create a dictionary

example:

fruits = ['apple', 'mango', 'banana','cherry']
print({f:len(f) for f in fruits})

another example:

cards = ['king', 'queen', 'jack', 'ace']

cards_dict = {card: card.upper() for card in cards}
print(cards_dict)

This comprehension iterates over each element card in the cards list.

card: card.upper() creates a key-value pair where the key is the original card and the value is card.upper(), converting the key to uppercase.

""" Nested Data Structures """

matrix = [
    [11, 12, 13, 14],
    [15, 16, 17, 18],
    [19, 20, 21, 22],
]

print([[row[i] for row in matrix] for i in range(4)])

this takes the items in a line = 11, 15, 19 - 12, 16, 20 etc

The code [row[i] for row in matrix] for i in range(4) does exactly this:

for i in range(4): This means "do this 4 times," once for each column.

[row[i] for row in matrix]: This means "take the i-th block from each row" and make a new list.

Another example:

payroll = {'emp1': {'name': 'Precious', 'job': 'Mgr', 'Wage': 50000},
     'emp2': {'name': 'Kim', 'job': 'Dev', 'Wage': 60000},
     'emp3': {'name': 'Sam', 'job': 'Dev', 'Wage': 70000}}

print(payroll) = prints the above

print(payroll['emp1']['name']).  = prints precious
print(payroll['emp1'].get('salary')) = none - no salary defined
print(payroll['emp1'].get('Wage'))   = 50,000
payroll['emp4'] = {'name': 'Max', 'job': 'Admin', 'Wage': 30000}
print(payroll)
del payroll['emp3'].  = deletes Sam

for id, info in payroll.items():
    print(f'\nEmployee ID: {id}')
    for key in info:
        print(f'{key} : {info[key]}')

        this prints for each person

        Emplyee ID: emp1
        name: precious
        job: mgr
        wage: 50000

Another example: - this is a list with two dictionarys nested inside

student_data = [
    {
        'name': 'John Smith',
        'email': 'john@gmail.com',
        'subjects': ['Math', 'Psychology', 'Physics', 'Chemistry', 'Biology']
    },
    {
        'name': 'Mary Jones',
        'email': 'mary@gmail.com',
        'subjects': ['Fine Art', 'Music', 'Biology', 'Geography', 'Politics']
    }]
print(student_data)

""" Variable Naming Conventions """

A function within a class is known as a method

def divide(num1, num2): = function
return num/num2

Classes = class names should have he first character capitalised - class ComplexNumber

""" Function Example"""

def lottery_generator():
       
    numbers = [] # Empty list to hold the numbers
    for number in range(0, 10):
		# randint() generates random integers
        numbers.append(randint(1, 50))
    return numbers

print(f"This weeks winning lottery numbers are {lottery_generator()}")

""" Defining functions"""

def tells computer we are creating a function

example:

def print_message():
    print("Hello World!")

print_message()

There is another type of function in python known as a "lambda" = anonymous

add = lambda a, b : a + b
print(add(5, 12)) 

this prints 17

example of calling an input to add my name and age, then returning it back to me:

# 2. This function runs for the name and age function calls
def get_user_input(prompt):
    return input(prompt)

# 4. This function runs twice
def print_out_to_console(value_to_be_printed):
    print(value_to_be_printed)

# 1. name and age are the first two function calls to run sequentially
name = get_user_input("Input your name:")
age = get_user_input("Input your age:")

# 3. Then function calls run sequentially
print_out_to_console(f"Your name is {name}")
print_out_to_console(f"You are {age} years old")

functions can also use optional parameters
def print_message(name='World):
    return f'hello {name}
    prints hello world


Example:

def three_num(num1, num2, num3):
    sum = num1 + num2 - num3
    print(sum)
three_num(10,20,10) = 20

another example:

def add_numbers(nums_tuple, min_value):
    total_sum = sum(num for num in nums_tuple if num >= min_value)
    return total_sum
    
total = add_numbers((21, 4, 7, 19, 1), 15)
print(total) = 40 (21+19) as these are the only numbers >= 15

""" Splat! *args * **kwargs"""

Allow to pass many arguments

*args = can be renamed at a latter time
**kwards = similar to *args but is used when a i use a keyword or named argument

def addition(a, b):
    return a + b

print(addition(2,2))

def add_integers(list_integers):
	total = 0
	for x in list_integers:
		total += x
	return total

list_integers = [1, 2, 3, 4]
print(add_integers(list_integers))

def add_many_integers(*integers):
	# Rename *args to something suitable
	total = 0
	for x in integers:
		# As it is a tuple you can use the in keyword to iterate 
		total += x
	return total

print(add_many_integers(1,2,3,4,5,6,7,8,9))

def concatenate_words(**words):
	result = ""
	# As **kwargs is a dict you need to iterate over .values()
	for arg in words.values():
		result += arg
		result += " "
	return result

print(concatenate_words(a='This', b="is", c="a", d="useful", e="feature"))

Another Example:

def make_string(*strings):
    return ' '.join(strings)

my_string = make_string("Alderaan", "Coruscant", "Dagobah", "Endor", "Hoth")
print(my_string)

def get_age(**data):
    return data.get('age', "no age provided")

pats_age = get_age(name="pat", level=4, age=33, occupation="postman")
print(pats_age)

