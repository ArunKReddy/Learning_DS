# absolute value of a number:
print("Absolute value of a number : ", abs(-3.74))
print("Absolute value of a number : ", abs(-3+5j))

print("***************all() Function*************************************")
# Check if all items in a list are True
mylist_true = [True, True, True]
print("Checking all the items in the list are : ", all(mylist_true))

mylist_false = [True, True, False]
print("Checking all the items in the list are : ", all(mylist_false))

mylist_list = [1, 2, 3]
print("Check if all items in a list are True : ", all(mylist_list))

mytuple = (0, True, -1)
print("Check if all items in a tuple are True : ", all(mytuple))

mylist_set = {0, 2, -4}
print("Check if all items in a set are True : ", all(mylist_set))

# Returns False because the first key is false.
# For dictionaries the all() function checks the keys, not the values.

mylist_dict = {0 : "Apple", 1 : "Orange"}
print("Check if all items in a dictionary are True : ", all(mylist_set))

print("***************ascii() Function*************************************")

print(ascii("My name is Akruthi"))

print("***************bin() Function*************************************")

print("Binary version : ", bin(50))

print("***************Sorted() Function*************************************")

my_sorted_list = [20, 65, 1, 3, 5]
print("Sorted list : ", sorted(my_sorted_list))

print("***************Sum() Function*************************************")

print("Sum of the list : ", sum(my_sorted_list))

print("***************Range() Function*************************************")
for x in range(10):
    print("Range function : ", x)

print("***************Reversed() Function*************************************")
alph = ["a", "b", "c", "d"]
rev = reversed(alph)

for x in rev:
    print("Reversed elements : ", x)

print("***************Zip() Function*************************************")
a = ("John", "Charles", "Mike", "Jim")
b = ("Jenny", "Christy", "Monica", "Vicky")
x = zip(a, b)
# use the dict() function to display a readable version of the result:
print("Dictionary : ", dict(x))

print("***************Filter() Function*************************************")
ages = [29, 30, 35, 15, 21, 12]

def my_func(x):
    if x < 18:
        return False
    else:
        return True

adults = filter(my_func, ages)

for i in adults:
    print("Age greater than 18 are : ", i)