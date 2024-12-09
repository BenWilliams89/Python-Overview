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
