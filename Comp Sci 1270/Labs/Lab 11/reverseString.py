# Gavin King           12/11/2025

# Code to reverse a strings

def reverseString(a):
    result = ""
    for i in range(0, len(a)):
        new = a[-i-1]
        result = result + new
    return result





def main():
    word = input("What word do you want to reverse? ")
    result1 = reverseString(word)
 
    print(result1)


if __name__ == "__main__":
    main()