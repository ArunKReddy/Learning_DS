# @Maddy : Solved all the below assignments

# 1. Problem 1: Handle the exception thrown by the code below by using try and except blocks.
try:
    for i in ['a','b','c']:
        print (i**2)
except TypeError:
    print('String cant be sqaured!!! Please try again')


# 2. Problem: Handle the exception thrown by the code below by using try and except blocks.
#    Then use a finally block to print 'All Done.'

try:
    x=5
    y=0

    z= x / y
except ZeroDivisionError:
    print("Can't Divide by Zero.. Please try again")

finally: print("All Done...")

# 3. Write a function that asks for an integer and prints the square of it.
#    Use a while loop with a try,except, else block to account for incorrect inputs.

def ask():
    while True:
        try:
            val = int(input('Enter the Integer : '))
        except:
            print("Looks like you did not enter an integer!")
            continue
        else:
            print("Thank you, you number squared is:", val**2)
            break
        finally:
            print('Finally I get Executed!!!')


ask()