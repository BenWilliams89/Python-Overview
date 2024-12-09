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
print(type('hello)) """ prints class 'str' """ for string

print(type(42)) """ prints class int - number'

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
