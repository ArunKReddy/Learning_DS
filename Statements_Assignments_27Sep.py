# @Maddy : All the scenarios solved.
# 1. Use for, split(), and if to create a Statement that will print out words that start with 's':

st1 = 'Print only the words that start with s in this sentence'

letters = st1.lower().split(" ")
my_list_start = []
for s2 in letters:
    if s2[0] == 's':
        my_list_start.append(s2)

print(my_list_start)



# 2. Use range() to print all the even numbers from 0 to 10.

def Even_Numbers():
    for x in range(1, 11):
        if x % 2 == 0:
            print("The Even in the given range are : ", x)
    x += 1

Even_Numbers()

# 3. Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

my_list = []

for x in range(1, 50):
    if x % 3 ==0:
        my_list.append(x)


print("All the numbers between 1 and 50 that are divisible by 3 using list comprehension : ",my_list)

# 4. Go through the string below and if the length of a word is even print "even!".

st = 'Print every word in this sentence that has an even number of letters'

my_words = st.split(" ")

for x in my_words:
    if (len(x)) % 2 == 0:
        print("The Even number of the letter are : ", x)

print('*******************************************************************************************')
# 5. Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for x in range(1, 100):
    if x % 5 == 0 and x % 3 == 0:
        print("FizzBuzz", x)
    else:
        if x % 3 == 0:
            print("Fizz", x)
        else:
            print('Buzz', x)

# 6. Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'

capturedstring = st.split(" ")

my_three_words = []

for x1 in capturedstring:
    my_three_words.append(x1[0:3])

print(my_three_words)

