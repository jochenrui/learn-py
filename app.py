2 + 2
x = 1
print(x)

# Typing
# Python is a dynamic language. Since Python3 we can use Typing
# Linters help to find Type Errors
age: int = 20
age = "python"  # mypy Linter shows an error here
print(age)

# immutability of primitive types
x = 1
print(id(x))  # some memory address
x = x + 1
print(id(x))  # new memory address because value change

# mutable types
mutable_array = [1, 2, 3]
print(id(mutable_array))  # some memory address
mutable_array.append(4)
print(id(mutable_array))  # same memory address

# Strings
some_string = 'python programming'
print(len(some_string))  # length of the String
print(some_string[0])  # access Chars in String by Index
print(some_string[-1])  # negative Index starts over from the back again
print(some_string[0:3])  # slice String [inclusiveStart, exclusiveEnd]
print(some_string[:3])
print(some_string[0:])

# some string methods -> ctrl + space to find more
print(some_string.casefold())
print(some_string.capitalize())
print(some_string.count("p"))
print(some_string.isalnum())

# find substring
print("programming" in some_string)
print("programming" not in some_string)
index_of: int = some_string.casefold().find("PRO".casefold())
# len(string|collection) is the prefered way to get the length
print(some_string[index_of:index_of+len("pro")])
# __method__() methods are special and shouldn't be called directly
print(some_string[index_of:index_of+"pro".__len__()])


# multi line string with linebreak
print("""This
is
a multi line String""")
print("This\nis\na multi line String")

# Special Characters in String
# backslash \ is used to escape special characters
escaped_quotes = "python \"programming\""
print(escaped_quotes)

# String concatenation & formated Strings

first_name = "jochen"
last_name = "rui"
# formated String f"" -> replaces values at runtime
full = f"{first_name} {last_name}"
print(full)

full_concat = first_name + " " + last_name
print(full_concat)

# Conditions

age = 22
if age >= 18:
    print("adult")  # indentation for if else
elif age >= 13:
    print("teenager")
else:
    print("child")

if x > 1:
    pass  # pass indicates empty block
else:
    pass

# Logical operators
name = "Jochen"
if not name:
    print("Name is empty")
else:
    print("Name not empty")

if age >= 18 and age < 65:
    print("Eligible")

if 18 <= age < 65:  # Chaining comparison operators is possible in Python
    print("Also eligible")

# ternary operator

message = "Eligible" if age >= 18 else "Not eligible"
print(message)

# loops

for y in "Python":  # loop over string
    print(y)

for y in ['a', 'b', 'c']:  # loop over array
    print(y)

for i in range(5):  # loop over range 0 - 4 (length: 5)
    print(y)

for i in range(0, 10, 2):  # inclusiveStart, exclusiveEnd, step
    print(y)

# range
# range != array
# range takes very small amount of memory compared to array/list

print(range(5))  # creates instance of Class "range"
print([1, 2, 3, 4, 5])  # creates an array

# loop + if else

# not clean way:
names = ["John", "Mary", "Jean"]
# names = ["Mary", "Doe"]

# not clean way:
found = False
for name in names:
    if name.startswith("J"):
        print(f"{name} found. Terminated")
        found = True
        break
    else:
        print(f"{name} doesn't start with J")
if not found:
    print("No J found")

# cleaner way:
for name in names:
    if name.startswith("J"):
        print("Found")
        break
else:  # executes else if for terminates, i.e. no J found
    print("Not found")

guess = 0
answer = 5
# while answer != guess:
#     guess = int(input("Guess: "))  # input takes user input from terminal
# else:
#     print("Correct")  # executed if while finishes succesfully

# Functions


# default value for parameter by=1
# typing for number & by
# return type: -> tuple
def increment(number: int, by: int = 1) -> tuple:
    return (number, number + by)  # returns tuple "read-only list"


print(increment(2, 3))
# keyword argument:
print(increment(3, by=5))
print(increment(4))


# asterix * indicates any amount of values (var args)
def multiply(*values):
    total = 1

    for number in values:
        total *= number
    return total


print(multiply(2, 3, 4, 5))


# double asterix ** allows to pass dictionary with any attributes
def save_user(**user):
    print(user)


# use double asterix ** function by passing key-value pairs
save_user(id=1, name="admin")

# Scope

# no block scope in Python, variable inside block is accessible from outside


def greet():
    message = "b"  # doesn't overwrite existing global variable message. Python creates a local variable with same name to work with
    # alternative: global message (global keyword) -> bad practice
    print(message)


greet()
print(message)


# F9 - create breakpoint
# F5 - start debug session
# F10 - go to next line of code
# F11 - go into function
# SHIFT + F11 - exit function


print("start")
print(multiply(1, 2, 3))

print("finish")

# fizzbuzz


def fizz_buzz(input):
    output = ''
    if input % 5 is 0:
        output += 'fizz'

    if input % 3 is 0:
        output += 'buzz'

    if len(output) is 0:
        output = input

    print(output)


fizz_buzz(5)
fizz_buzz(3)
fizz_buzz(7)
fizz_buzz(15)
