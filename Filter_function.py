# filter function using lambda:
# filter function takes in a function and list as arguments. This offers an elegent way to filter
# out all the elements of a sequence, for which the functions returns True.

# small program that returns the odd numbers from the list.
li = [19, 2, 10, 11, 13, 17, 1, 20]

final_list = list(filter(lambda x : (x%2 != 0), li))
print("Using filter function : ", final_list)

# Use lambda() and map()
final_map_list = list(map(lambda x : x**2, li))
print("Using map function : ", final_map_list)

