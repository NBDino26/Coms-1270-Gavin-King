# Gavin King           12/11/2025

# Solving Fizz buzz 

def fizzBuzzModulus(a):
    if (a % 3 == 0) and (a % 5 == 0):
        return "FizzBuzz"
    elif a % 3 == 0:
        return "Fizz"
    elif a % 5 == 0:
        return "Buzz"
    elif a % 7 == 0:
        return "Bizz"
    else:
        return "i"
    

    

def main():
    num = int(input("What number do you wish to test? "))
    answer1 = fizzBuzzModulus(num)

    print(answer1)


if __name__ == "__main__":
    main()