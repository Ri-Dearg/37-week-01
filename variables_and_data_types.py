# variables_and_data_types.py
# Declaring variables, the core Python data types, checking a value's
# type, and converting between types.

#  ---------- Variables ----------
# A variable is a name that holds a value. The = sign assigns the
# value to the name.
greeting = 'Hello, world!'
print(greeting)

# A variable can be reassigned at any time. The new value replaces the old.
greeting = 'Hello, students!'
print(greeting)

# ---------- Data Types ----------
# Python figures out the type from the value you assign.

# String (str): text wrapped in single or double quotes.
# Choice is largely stylistic.
first_name = 'John'
last_name = "Doe"

# Integer (int): a whole number, positive or negative.
age = 36
score = -10

# Float (float): a number with a decimal point.
price = 19.99
discount = .25

# Boolean (bool): either True or False. The capital letter matters.
is_logged_in = True
is_admin = False

# NoneType (None): a placeholder meaning "no value yet".
# Most common use at this stage is for debugging.
selected_option = None

#  ---------- Determining the Data Type ----------
# type() returns the data type of a value. Useful when something is
# behaving unexpectedly and you want to confirm what you're working with.
print(type(first_name))      # <class 'str'>
print(type(age))             # <class 'int'>
print(type(price))           # <class 'float'>
print(type(is_logged_in))    # <class 'bool'>
print(type(selected_option)) # <class 'NoneType'>

# ---------- User Input ----------
# input() waits for the user to type in the
# terminal, then returns what they typed as a string.
# Run this from the terminal: python variables_and_data_types.py

user_name = input('What is your name? ')
print('Hello, ' + user_name)

#  ---------- Converting Between Data Types ----------
# input() always returns a string, even if the user types numbers.
# Convert with int(), float(), or str() to use the value differently.

# String to integer
age_text = '36'
age_number = int(age_text)
print(age_number + 4)    # 40

# String to float
price_text = '19.99'
price_number = float(price_text)
print(price_number * 2)  # 39.98

# Integer to string (needed when joining a number with text using +)
items_in_cart = 3
print('You have ' + str(items_in_cart) + ' items in your cart.')

# F-strings, looked at in the future, are often clearer to use.
print(f'You have {items_in_cart} items in your cart.')

# Float to integer truncates, it does not round.
print(int(10.8))         # 10

# Putting it together: input -> convert -> calculate -> convert back
age_input = input('How old are you? ')
age_in_ten_years = int(age_input) + 10
print('In 10 years you will be ' + str(age_in_ten_years))
