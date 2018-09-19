var = "Hello Strings"
print(var)

print("The Zero character of a String : " +var[0])
print("The Characters from 1 to 4th in var variable is : " + var[1:4])

# Strings concatenation

var1 = "Akruthi"
var2 = "Arun"

print("String Concatenation from two Strings : "+var1[1:4]+var2[0:2])

a = "Akruthi"
b = 99
c = a+str(b)
print(c*2)

#More Examples - Using other STRING Operators

# Using 'IN' Operator
a = "Akruthi"
print("k" in a)

# Using 'Not IN' Operator
b = "Aishu"
print("A" not in b)

# % Used for the String format
Name = "Akruthi"
Number = 99
print('%s %d' %(Name, Number))

# Python String replace() method
oldString = 'Akruthi likes Arun'
newString = oldString.replace('likes','loves')
print(newString)

# Changing upper case and lower case strings
string = "Python Rocks!!!"
print(string.upper())
print((string.capitalize()))

string1 = 'PYTHON WOW!!!'
print(string1.lower())

# Using Join function for the string
print((":".join("Python")))

# Reversing the string
String = "12345"
print("".join(reversed(String)))

# Splitting the word
words = 'Arun Aishu Akruthi'
print(words.split(" "))

# Strings are mutable
x="Akruthi"
x1 = x.replace("Akruthi","Aishu")
print("New Modifiying string : "  + x1)
print("After Modifiying the old String : " + x)
print("----------------------------------------------------------------")
print("---------------Python TUPLE--------------------------------------")

# Python TUPLE - Pack, Unpack, Compare, Slicing, Delete, Key

# Tuple with list of elements
tup = ('Jan','Feb','March')
print(tup)

# Empty tuple
tup1 = ()
print(tup1)

# tuple with single element
tup2 = (50,)
print(tup2)

tup3 = ('chidu','kulkarni','Dzire','RR Nagar')
tup4 = (1,2,3,4,5,6,7,8,9)

print(tup3[0:2] + tup4[1:4])
print(tup4[1:4])

print("----------Packing and UnPacking----------")

# Tuple packing
x = ('Akruthi',3,'PEP School')

# Tuple unpacking
(Name,Age,School) = x

print("Name :" + Name)
print("Age : " + str(Age))
print("School Name : "+School)

print("----------Comparing Tuples----------")
FirstTuple=(1,4)
SecondTuple=(3,2)
if (FirstTuple>=SecondTuple):
    print("FirstTuple is Bigger")
else:
    print("SecondTuple is Bigger")

print("----------Using tuples as keys in dictionaries-----------------------")

a1 = {'x' : 100, 'y' : 200}
b = list(a1.values())
c = list(a1.items())
print(b)
print(c)

print("-------------Slicing of Tuple--------------------------------")

x = ("a","b","c","d","e","f")
print(x[1:4])
print(len(x))

