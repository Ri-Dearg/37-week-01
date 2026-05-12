# ---------- String Formatting (Concatenation) ----------
# Use + to join strings together.
first_name = 'john'
last_name = 'doe'
full_name = first_name + ' ' + last_name
print(full_name)  # john doe

# To include a number, convert it to a string first.
age = 36
print(full_name + ' is ' + str(age) + ' years old.')

# print() can also take multiple arguments separated by commas.
# It adds a space between them automatically.
# I normally only do this for debugging.
print(full_name, 'is', age, 'years old.')

# ---------- String Methods ----------
# A method is a type of function attached to a value, called with a dot.
message = '  Hello, World!  '

# Case conversion
print(message.upper())   # '  HELLO, WORLD!  '
print(message.lower())   # '  hello, world!  '
print(message.title())   # '  Hello, World!  '

# .strip() removes whitespace from both ends.
print(message.strip())   # 'Hello, World!'

# .replace() swaps one substring for another.
print(message.replace('World', 'Python'))  # '  Hello, Python!  '

# len() returns the length (it's a built-in function, not a method).
print(len('Python'))     # 6

# 'in' checks whether a substring exists inside another string.
print('x' in message)  # True

# Methods can be chained: each returns a new string the next can act on.
cleaned = message.strip().lower().replace('world', 'python')
print(cleaned)  # 'hello, python!'

# There are also methods for validation that return True or False
message.isalpha()   # True
message.isnumeric() # False

# ---------- F-Strings ----------
# Put f before the opening quote, then use {} to embed variables
# directly in the string. No conversion needed.
# Very straightforward and readable.
print(f'{full_name} is {age} years old.')

# Expressions are allowed inside the braces.
print(f'Next year, {full_name} will be {age + 1}.')

# String methods work inside braces too.
print(f'Hello, {full_name.title()}!')

# Ignore for now
# # Number formatting: :.2f rounds to 2 decimal places.
# print(f'Price: ${price:.2f}')   # Price: $19.99

# ---------- Putting it together ----------
# Cleaning input, using a method, and formatting output with an f-string.
raw_input = '  john doe  '
name = raw_input.strip().title()
birth_year = 1815
current_year = 2026
years_alive = current_year - birth_year
print(f'{name} would be {years_alive} years old today.')
