# Python Learning Path: Basic Guide 
# by Allan Castro: https://github.com/alcastrocr

# ---------------------------------------------------------
# 1. Introduction to Python
# ---------------------------------------------------------
# Python is a versatile programming language widely used in web development, data science, 
# automation, artificial intelligence, and more. Known for its simplicity and readability, 
# Python is a great choice for beginners and professionals alike.

# ---------------------------------------------------------
# 2. Setting Up a Local Development Environment
# ---------------------------------------------------------
# To run Python code, you need to have Python installed on your computer. 
# Here are the steps to set up your local Python development environment:

# Step 1: Install Python
# --------------
# - Go to the official Python website: https://www.python.org/downloads/
# - Download the latest version of Python for your operating system (Windows, macOS, or Linux).
# - During installation on Windows, make sure to check the box that says "Add Python to PATH". This will make it easier to run Python from the command line.

# Step 2: Install an Integrated Development Environment (IDE) or Text Editor
# --------------
# Python code can be written in any text editor, but using an IDE (Integrated Development Environment) or a specialized code editor will make coding easier.
# My personal favorite:
# - Visual Studio Code (VS Code) - A lightweight and powerful editor that supports Python with extensions. 
#     - Download here: https://code.visualstudio.com/
#     - After installing, open VS Code and install the Python extension from the marketplace to enable Python support.

# Step 3: Run Your First Python Program
# --------------
# Now that your environment is set up, you can start coding! 
# Open your IDE or text editor, create a new Python file (with the `.py` extension), and write your first Python program.

# Example:
print("Welcome to Python Programming!")  # This will print "Welcome to Python Programming!" on the screen.

# Exercise: Install Python, set up an IDE, and write code to print a greeting message like "Hello, Python World!"
# Solution:
print("Hello, Python World!")  # Output: Hello, Python World!

# Now you're ready!

# ---------------------------------------------------------
# 3. Basic Syntax and Printing
# ---------------------------------------------------------
# Python uses indentation to define code blocks. The `print()` function is used to display 
# information on the screen.

# Example 1: Simple print statements
print("Learning Python is fun!")
print("5 + 3 =", 5 + 3)  # Outputs: 5 + 3 = 8

# Example 2: Combining strings and variables
name = "Allan"
print("Hello, " + name + "!")  # Output: Hello, Allan!

# Exercise: Write a program to print your name and your favorite hobby.
# Solution:
my_name = "Allan"
hobby = "reading"
print(f"My name is {my_name} and I love {hobby}.")  # Output: My name is Allan and I love reading.

# ---------------------------------------------------------
# 4. Variables
# ---------------------------------------------------------
# Variables store data. Python is dynamically typed, so you don't need to declare the type.

# Example: Variable assignment
age = 36  # Integer
height = 169.5  # Float
is_hungry = True  # Boolean
name = "Allan"  # String
print(f"{name} is {age} years old and {height} centimeters tall. Hungry: {is_hungry}")

# Exercise: Create variables for your favorite movie, age, and a fact about yourself.
# Solution:
favorite_movie = "Inception"
my_age = 36
fun_fact = "I love coding!"
print(f"My favorite movie is {favorite_movie}, I am {my_age}, and {fun_fact}.")

# ---------------------------------------------------------
# 5. Basic Math Operations
# ---------------------------------------------------------
# Python supports arithmetic operations: addition (+), subtraction (-), multiplication (*), 
# division (/), modulus (%), exponentiation (**), and floor division (//).

# Example: Math operations
x = 10
y = 3
print(f"Addition: {x + y}, Subtraction: {x - y}, Multiplication: {x * y}")
print(f"Division: {x / y}, Modulus: {x % y}, Exponentiation: {x ** y}")

# Exercise: Write code to calculate the area of a rectangle.
# Solution:
length = 6
width = 4
area = length * width
print(f"The area of the rectangle is {area} square units.")  # Output: The area of the rectangle is 24 square units.

# ---------------------------------------------------------
# 6. Control Flow
# ---------------------------------------------------------
# Control flow uses `if`, `elif`, and `else` statements to make decisions.

# Example: If-else statements
temperature = 18
if temperature > 25:
    print("It's a hot day!")
elif temperature > 15:
    print("It's a warm day!")
else:
    print("It's a cold day!")

# Exercise: Write code to check if a number is positive, negative, or zero.
# Solution:
number = -5
if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# ---------------------------------------------------------
# 7. Loops
# ---------------------------------------------------------
# Loops allow repetitive tasks. Python has `for` loops and `while` loops.

# Example 1: `for` loop
for i in range(5):
    print(f"Number: {i}")

# Example 2: `while` loop
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1

# Exercise: Write a loop to print the first 10 square numbers.
# Solution:
for i in range(1, 11):
    print(f"{i} squared is {i ** 2}")

# ---------------------------------------------------------
# 8. Functions
# ---------------------------------------------------------
# Functions are reusable blocks of code. Define a function using `def`.

# Example: Function definition
def greet(name):
    return f"Hello, {name}!"

print(greet("Allan"))  # Output: Hello, Allan!

# Exercise: Write a function to calculate the sum of two numbers.
# Solution:
def add_numbers(a, b):
    return a + b

print(f"The sum of 5 and 7 is {add_numbers(5, 7)}")  # Output: The sum of 5 and 7 is 12.

# ---------------------------------------------------------
# 9. Lists
# ---------------------------------------------------------
# Lists store ordered collections of items.

# Example: List operations
fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Outputs: banana
fruits.append("orange")
print(fruits)  # Outputs: ['apple', 'banana', 'cherry', 'orange']

# Exercise: Create a list of your favorite foods and print the first item.
# Solution:
favorite_foods = ["pizza", "sushi", "pasta"]
print(f"My favorite food is {favorite_foods[0]}")  # Output: My favorite food is pizza.

# ---------------------------------------------------------
# 10. Dictionaries
# ---------------------------------------------------------
# Dictionaries store key-value pairs.

# Example: Dictionary operations
person = {"name": "Allan", "age": 36}
print(person["name"])  # Outputs: Allan
person["age"] = 36
print(person)  # Outputs: {'name': 'Allan', 'age': 36}

# Exercise: Create a dictionary for your favorite book with title and author keys.
# Solution:
favorite_book = {"title": "1984", "author": "George Orwell"}
print(f"My favorite book is '{favorite_book['title']}' by {favorite_book['author']}.")

# ---------------------------------------------------------
# 11. Error Handling
# ---------------------------------------------------------
# Handle errors gracefully using try-except blocks.

# Example: Try-except for error handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Exercise: Write code to handle invalid user input for converting a string to an integer.
# Solution:
user_input = "abc"
try:
    number = int(user_input)
except ValueError:
    print("Invalid input! Please enter a number.")

# ---------------------------------------------------------
# 12. Final Project: Contact Book
# ---------------------------------------------------------
# Combine learned concepts to create a simple contact book.

contacts = {}

def add_contact(contacts, name, phone):
    contacts[name] = phone

def view_contacts(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

# Adding and viewing contacts
add_contact(contacts, "Allan", "506-8888-8888")
view_contacts(contacts)
