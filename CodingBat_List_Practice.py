# Given an array of ints, return True if 6 appears as either the first or last element in the array.
# The array will be length 1 or more.

def first_last_six(nums):
    return (nums[0] ==6 or nums[-1] == 6)


print(first_last_six([13, 6, 1, 2, 6]))

print("****************************************************")

def make_pi(l):
    return [3, 1, 4]


# li = list(map(make_pi, [1, 2, 3]))
# print(li)

print("*******************************************************")

# Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element.
# Both arrays will be length 1 or more.


def common_end(a, b):
    return (a[:1] == b[:1]) or (a[-1:] == b[-1:])


print(common_end([1, 2, 3], [1, 3]))

print("*******************************************************")

# Given an array of ints length 3, return the sum of all the elements.

def sum_array(nums):
    return sum(nums)


print(sum_array([1, 2, 3]))

print("*******************************************************")

# Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}
def rotate_left(nums):
    return nums[1:]+nums[:-2]


print(rotate_left([1, 2, 3]))

print("*******************************************************")

# Given an array of ints length 3, return a new array with the elements in reverse order,
# so {1, 2, 3} becomes {3, 2, 1}.

def reverse3(nums):
    return list(reversed(nums))

print(reverse3([1, 2, 3]))

print("*******************************************************")

# Given an array of ints length 3, figure out which is larger, the first or last element in the array,
# and set all the other elements to be that value. Return the changed array.


def max_end3(nums):
    if nums[:1] > nums[-1:]:
        return nums[:1] * 3
    else:
        return nums[-1:] * 3


print(max_end3([11, 5, 9]))
print("*******************************************************")

# Given an array of ints, return the sum of the first 2 elements in the array.
# If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.

def sum2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 2:
        return sum(nums)
    elif len(nums) == 1:
        return sum(nums)
    else:
        return sum(nums[0:2])


print(sum2([1, 1, 1, 1]))

print("*******************************************************")

# Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
def middle_way(a, b):
    return a[1:2] + b[1:2]


print(middle_way([1, 2, 3], [4, 5, 6]))
print("*******************************************************")

# Given an array of ints, return a new array length 2 containing the first and last elements from the original array.
# The original array will be length 1 or more.
def make_ends(nums):
    return nums[0:1]+nums[-1:]


print(make_ends([1, 2, 3]))
print("*******************************************************")

# Given an int array length 2, return True if it contains a 2 or a 3.
def has23(nums):
    if nums.count(2) or nums.count(3):
        return True
    else:
        return False


print(has23([4, 5]))

print("*******************************************************")

# Given an array of ints, return True if the array is length 1 or more,
# and the first element and the last element are equal.

def same_first_last(nums):
    if (nums[0:1] == nums[-1:]) and len(nums) > 1:
        return True
    elif len(nums) == 1:
        return True
    else:
        return False



print(same_first_last([1]))

# len(nums) == 1 and

