# 1.Write a function that computes the volume of a sphere given its radius.

def vol(rad):
    return 4/3 * 3.14 * rad * rad * rad


print(vol(3))

# 2. Write a function that checks whether a number is in a given range (Inclusive of high and low)

def ran_check(num, low, high):
    if num in range(low, high):
        print('Number is in the given range', num)
    else:
        print('Number is not in range', num)


print(ran_check(4, 2, 6))

# 3. Write a function that checks whether a number is in a given range (Inclusive of high and low) - Returns boolean

def ran_bool(num, low, high):
    if num in range(low, high):
        return True
    else:
        return False


print(ran_bool(4, 2, 6))

#4. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.


def up_low():
    s = 'Hello Mr. Rogers, how are you this fine Tuesday?'

    # Lower Case Letters
    print('Lower Case Count : ', sum(map(str.islower, s)))
    print('Second way : Lower Case Count : ', sum(1 for l in s if l.islower()))

    # Upper Case letters
    print('Upper Case Count : ', sum(1 for c in s if c.isupper()))


print(up_low())

# 5. Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(l):
    final_list = []
    for num in l:
        if num not in final_list:
            final_list.append(num)
    return final_list


l = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]
print(unique_list(l))

# 6. Write a Python function to multiply all the numbers in a list.

sample_list = [1, 2, 3, 4]

def multiply_numbers(sample_list):
    pass
