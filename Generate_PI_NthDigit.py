import math

precision = int(input("How many spaces? "))

while precision > 50:
    print("Number to large")
    precision = int(input("How many spaces? "))
else:
    print('%.*f' % (precision, math.pi))