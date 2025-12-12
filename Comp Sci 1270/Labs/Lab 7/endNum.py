# Gavin King            10-28-25
# Lab Week 7


number = ""
numbers = []


def listCreation(number):
    intNumbers = []
    while number != "*":
        number = input("Input a number into a list. Input will end when * is inputted ")
        numbers.append(number)
    numbers.remove("*")   
    for i in numbers:
        intNumbers.append(int(i))
    return(intNumbers)

def endNum(num, list):
    for i in range(len(list)):
        if list[i] == num:
            list.remove(num)
            list.append(num)
        return(list)




def main():
    intNumbers = listCreation(0)
    num = input("Input a number to be at the end of your list: ")
    neList = endNum(num, intNumbers)
    print(neList)




if __name__ == "__main__":
    main()