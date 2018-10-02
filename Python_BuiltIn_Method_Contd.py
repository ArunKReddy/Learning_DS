print("***********Map() function**************************")
# Calculate the length of each word in the tuple:
def my_len(n):
    return len(n)


x = map(my_len, ('Akruthi', 'Aishu', 'Arun'))
for i in x:
    print("Length of the word : ", i)

print("***********pow() function**************************")

print("Return the value of 4 to the power of 3 (same as 4 * 4 * 4): ", pow(4, 3))