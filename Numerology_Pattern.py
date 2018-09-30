while True:
    try:
        num = int(input("Enter the number from 0 to 9: "))

        if num == 0:
            print("You are think just like Aryabhatta!!!")

        elif num == 1:
            print("This is a strong number which speaks about power, authority.")

        elif num == 2:
            print("perfect number for people who love art and music and are romantic.")

        elif num == 3:
            print("number represents expansion, ambition, management")

        elif num == 4:
            print("number represents smart mind but restless and instable")

        elif num == 5:
            print("number represents change, busy life")

        elif num == 6:
            print("best number for home makers")

        elif num == 7:
            print("strongest mystical number")

        elif num == 8:
             print("number is good for people who work for masses. ")

        elif num == 9:
             print("It can be a fortunate number. People with health issues should not keep this number.")

    except ValueError:
        print("Enter the valid input......")

    finally: print("All Done...")