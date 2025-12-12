# Gavin King            10-28-25
# Lab Week 7

number = ""
numbers = []
intNumbers = []


def listCreation(number):
    while number != "*":
        number = input("Input a number into a list. Input will end when * is inputted ")
        numbers.append(number)
    numbers.remove("*")   
    for i in numbers:
        intNumbers.append(int(i))


def findMin(list):
    pass

def findMax(list):
    pass






def main():
    listCreation(1)
    findMin(intNumbers)
    findMax(intNumbers)


if __name__ == "__main__":
    main()