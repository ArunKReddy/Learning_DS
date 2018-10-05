# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
def first_half(str):
  print(str[:len(str) // 2])


first_half('WooHoo')

# Given a string, return a version without the first and last char,
#  so "Hello" yields "ell". The string length will be at least 2.
def without_end(str):
    return (str[1:-1])


print(without_end("Hello"))

# Given 2 strings, a and b, return a string of the form short+long+short,
# with the shorter string on the outside and the longer string on the inside.
# The strings will not be the same length, but they may be empty (length 0).
def combo_string(a, b):
    if len(a) > len(b):
        return b+a+b
    else:
        return a+b+a


print(combo_string('Hello','hi'))

# Given 2 strings, return their concatenation, except omit the first char of each.
# The strings will be at least length 1.

def non_start(a, b):
    return a[1:]+b[1:]


print(non_start('Hello', 'There'))

# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end.
# The string length will be at least 2.

def left2(str):
    return str[2:]+str[:2]


print(left2('Hello'))