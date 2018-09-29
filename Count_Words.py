# problem 1: One Way : Counting the number of letters in the string.

def count_letters(word, char):
    count = 0
    for c in word:
        if char == c:
            count += 1
    return count


print(count_letters('bannana', 'b'))

# Problem 2: Count the number of occurance in the string
# Using Method 1:

a = 'google.com'
d = {x : a.count(x) for x in a}
print(d)

# Method 2: Using sets.
s = {y : a.count(y) for y in set(a)}
print(s)