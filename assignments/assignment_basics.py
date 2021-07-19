class Person:

    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    def __repr__(self) -> str:
        return f'name: {self.__name}, age: {self.__age}'

    def getAgeInDecades(self) -> int:
        return self.__age % 10


def printTwoValues(value1, value2):
    print(f'{value1} {value2}')


user_name = input("Enter your name:")

user_age = input("Enter your age:")

while not user_age.isdigit():
    user_age = input("Enter a valid age please")

# Task 1
jochen: Person = Person(user_name, int(user_age))

# Task 2
print(jochen.__repr__())

# Task 3
printTwoValues("hello", "world")

# Task 4
print(jochen.getAgeInDecades())
