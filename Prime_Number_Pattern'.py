num = int(input("Enter the Prime Number"))

if num == 1:
    print("The number neither prime nor composite")

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "Not Prime")
            break
    else:
        print(num, "Prime")