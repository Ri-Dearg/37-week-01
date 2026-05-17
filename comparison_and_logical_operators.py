# comparison_and_logical_operators.py
# Comparing values, combining truth conditions with and/or/not,
# and reading common error messages.

# Comparison Operators ----------
# Each one returns True or False.

# Equal to (note the double =, since single = is assignment)
print(5 == 5)    # True
print(5 == 6)    # False

# Not equal to
print(5 != 6)    # True

# Greater than / less than
print(10 > 3)    # True
print(10 < 3)    # False

# Greater than or equal / less than or equal
print(10 >= 10)  # True
print(10 <= 9)   # False

# Comparisons work with variables. The result is a boolean you can
# store, print, or use later.
score = 85
passing = score >= 60
print(passing)   # True

# Strings compare alphabetically (technically by character codes,
# so uppercase letters come before lowercase).
print('apple' == 'apple')   # True
print('apple' < 'banana')   # True
print('Banana' < 'apple')   # True (uppercase wins)

# Be careful comparing different types.
print('5' == 5)    # False (string vs int)
print(5 == 5.0)    # True  (int and float compare by value)

# Logical Operators ----------
# Combine or invert booleans with and / or / not.

age = 25
has_ticket = True

# 'and' is True only when BOTH sides are True
print(age >= 18 and has_ticket)   # True

# 'or' is True when EITHER side is True
print(age >= 65 or has_ticket)    # True

# 'not' flips True to False and vice versa
print(not has_ticket)             # False

# Combine them — use parentheses to make precedence clear.
is_weekend = False
is_holiday = True
print((is_weekend or is_holiday) and age >= 18)   # True

# Checking a value falls within a range:
temperature = 22
print(temperature >= 20 and temperature <= 30)   # True

# Python also allows the cleaner chained form:
print(20 <= temperature <= 30)                   # True
