# numbers_and_strings.py
# Arithmetic operators, increment/decrement shortcuts, string
# methods, and string formatting with f-strings.

# ---------- Arithmetic Operators ----------
# The basics: +, -, *, /
print(2 + 2)    # 4
print(10 - 3)   # 7
print(4 * 5)    # 20
print(10 / 4)   # 2.5  (division always returns a float)

# Floor division: divide and discard the remainder.
print(10 // 4)  # 2

# Modulus: the remainder after division.
print(10 % 3)   # 1

# Exponent: raise to a power.
print(2 ** 3)   # 8

# Operators work with variables too.
price = 19.99
quantity = 3
total = price * quantity
print(total)    # 59.97

# Order of operations follows standard maths (PEMDAS/BODMAS).
# Use parentheses to make intent clear.
print(2 + 3 * 4)    # 14
print((2 + 3) * 4)  # 20

# ---------- Incrementing & Decrementing ----------
# Python has no ++ or -- operator. Use += and -= instead.
score = 0
score += 1   # same as: score = score + 1
score += 5
print(score)  # 6

score -= 2
print(score)  # 4

# The same shortcut works for *, /, %, and **.
score *= 2
print(score)  # 8
