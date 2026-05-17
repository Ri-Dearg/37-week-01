# flow_control.py
# Making decisions in code with if / elif / else, understanding
# truthy and falsy values, ternary expressions

# ---------- If Statements ----------
# An 'if' statement runs a block of code only when its condition is True.
# The condition line ends with a colon. Everything indented underneath
# is the block that runs when the condition is True.
age = 16

if age > 18:
    print('You are old enough to vote.')
elif age == 18:
    print('You are JUST old enough to vote.')
else:
    print('You are NOT old enough to vote.')

# Indentation is part of Python's syntax. 4 spaces is the standard.
# When indentation goes back, the if-block ends.
print('This line always runs — it is outside the if.')


name = 'Ada'
if name:
    print(f'Hello, {name}')      # runs — non-empty strings are truthy

empty_name = ''
if empty_name:
    print('This will not print.')  # empty string is falsy

count = 5
if count:
    print(f'You have {count} items.')   # any non-zero number is truthy

# ---------- If, Else ----------
# 'else' runs when the 'if' condition is False.
score = 45

if score >= 60:
    print('Pass')
else:
    print('Fail')

# ---------- If, Elif, Else ----------
# 'elif' (else-if) lets you check multiple conditions in order.
# Python evaluates them top to bottom and runs the FIRST that is True.
score = 97

if score >= 90:
    if score >= 96:
        print('Grade: A+')
    elif score >=90:
        print('Grade: A-')
elif score >= 80:
    print('Grade: B')
elif score >= 70:
    print('Grade: C')
elif score >= 60:
    print('Grade: D')
else:
    print('Grade: F')

# ---------- Nested Flow Control ----------
# An 'if' can live inside another 'if'. Each level adds 4 more
# spaces of indentation.
is_logged_in = True
is_admin = True

if is_logged_in:
    if is_admin:
        print('Welcome, admin!')
    else:
        print('Welcome, user!')
else:
    print('Please log in.')

# Tip: too much nesting hurts readability. Often the same logic
# is clearer when you combine conditions with 'and':
if is_logged_in and is_admin:
    print('Welcome, admin!')
elif is_logged_in:
    print('Welcome, user!')
else:
    print('Please log in.')

# ---------- Ternary Expressions ----------
# A one-line shortcut for simple if/else. The pattern is:
#   value_if_true if condition else value_if_false
status = 'adult' if age >= 18 else 'minor'
print(status)

# Useful inside f-strings:
print(f"You {'passed' if score >= 60 else 'failed'} the test.")
