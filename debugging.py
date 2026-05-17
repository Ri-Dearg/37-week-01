
# Reading Error Messages ----------
# When code breaks, Python prints a "traceback". The most useful
# line is usually the LAST one: the error type and message.
# The examples below are commented out so the file still runs.
# Uncomment one at a time to see Python's response.

# SyntaxError: something is structurally wrong with the code.
# print('hello'

# NameError: a name was used that doesn't exist (often a typo).
# print(scor)

# TypeError: an operation was used on the wrong type.
# print('age: ' + 25)   # can't add a string and an int

# ValueError: the type is right but the value isn't valid.
# int('hello')

# ZeroDivisionError: yes, exactly what it sounds like.
# print(10 / 0)

# ---------- Debugging with print() and comments ----------
# When code doesn't behave the way you expect, two of the simplest
# tools are: drop print() in to inspect values, and use # to
# temporarily disable lines.

score = 85
bonus = 10
total = score + bonus

print(f'score = {score}')   # debug
print(f'bonus = {bonus}')   # debug
print(f'total = {total}')   # debug

if total >= 100:
    print('Excellent!')
elif total >= 80:
    print('Great job.')
else:
    print('Keep practicing.')

# Comments are also useful while debugging. To test without a line
# of code, prefix it with # instead of deleting it — easy to put back.
price = 100
# discount = 20
# price -= discount
print(f'Price: ${price}')