# Gavin King            10-28-25
# Lab Week 7

numbers = []


def rotateList(rot, list):
    rotList = []
    for i in range(list.len):
        rotList.insert(i, (list[i - rot]))


def listCreation(number):
    intNumbers = []
    while number != "*":
        number = input("Input a number into a list. Input will end when * is inputted ")
        numbers.append(number)
    numbers.remove("*")   
    for i in numbers:
        intNumbers.append(int(i))
    return(intNumbers)


 


def main():
    intNumbers = listCreation(0)
    rot = input("Input a number for rotations: ")
    rotateList(int(rot), intNumbers)


if __name__ == "__main__":
    main()