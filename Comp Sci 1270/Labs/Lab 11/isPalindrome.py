# Gavin King         12/11/2025

# This program will check if inputted string is a string

def isPalindromeIterative(a):
    result = False
    for i in range(0, len(a)):
        num = (-i-1)
        if a[i] == a[num]:
            result = True
        else:
            result = False
            break
    return result

def isPalindromeRecursive(a):
    if len(a) < 2:
        return True
    elif a[0] == a[-1]:
        new = a[1:-2]
        isPalindromeRecursive(new)
        return True
    else:
        return False
        
    
                

def main():
    word = input("What word do you wanna check? ")
    answer1 = isPalindromeIterative(word)
    answer2 = isPalindromeRecursive(word)
    print(answer1)
    print(answer2)

if __name__ == "__main__":
    main()
