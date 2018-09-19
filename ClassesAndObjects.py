class myclass():
    def method1(self):
        print("Akruthi")

    def method2(self,something):
        print("Printing : "+ something)

class myChildclass(myclass):
    def method3(self):
        print("Printing child class")

def main():
    c = myclass()
    c1=myChildclass()

    c.method2("Akruthi")
    c.method1()
    c1.method3()
    c1.method1()
    c1.method2("Aishu")


if __name__ == '__main__':
    main()
