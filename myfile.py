f= 100
print(f)

def my_func():
    global f
    print(f)
    f = 'This is global variable'

my_func()
print(f)