# If Statement
# def main():
#     x, y = 2, 4
#
#     if (x < y):
#         st = 'x is less than y'
#     print(st)
#
# if __name__ == '__main__':
#     main()



# def SwitchExample(argument):
#     switcher = {
#         0: "This is case 0",
#         1: "This is case 1",
#         2: "This is case 2",
#     }
#     return switcher.get(argument, "nothing")
#
# if __name__ == '__main__':
#     argument = 1
#     print(SwitchExample(argument))


# def main():
#     Months = ['Jan','Feb','Mar','Apr','May']
#
#     for m in Months:
#         print(m)
#
# if __name__ == '__main__':
#     main()


# def main():
#
#     for x in range(10,20):
#         if x == 15:
#             break
#         if x % 2 == 0: continue
#         print(x)
#
# if __name__ == '__main__':
#     main()


# How to use enumerate in for loop

def main():
    months = ['Jan', "Feb", "Mar", "Apr", "May"]
    for i,m in enumerate(months):
        print(i, m)


if __name__ == '__main__':
    main()