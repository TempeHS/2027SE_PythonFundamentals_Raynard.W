def main():
    number = getnumber()
    meow(number)


def getnumber():
    while True:
        n = int(input("What's n?"))
        if n > 0:
            return n


def meow(n):
    for i in range(n):
        print("meow")


main()

# for i in range(3):
#    print("meow")
