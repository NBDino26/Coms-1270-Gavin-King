# Gavin King    Lab 5   10-2-25
# This program makes a centered pyradmid made out of numbers

def numberPyramid(layers):
    for j in range(1, layers + 1):
        print(" " * (layers - j), end=" ")
        for i in range(1, j+1):
             
             print(i, end=" ")
        print("")

def main():
    numberPyramid(int(input("How many layers for your pyramid: ")))

if __name__ == "__main__":
    main()