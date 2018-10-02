# Removing the duplicates in the string.
print(set("my name is Eric and Eric is my name".split()))

a = set(['Arun', 'Aishu', 'Akruthi'])
print("List A contains : ", a)

b = set(['Aishu', 'Akruthi'])
print("List B contains : ", b)

# To find the common elements in both the sets. Using INTERSECTION method.
print("Attended Both the Events : ", a.intersection(b))

print("Attended Both the Events : ", b.intersection(a))

# Existance in any one of the group.
print("Attended only one event : ", a.symmetric_difference(b))

# Attended only one event and not the other.
print("Attended only one event not the other : ", a.difference(b))

# Present in both the groups.
print("list of all participants : ", a.union(b))

