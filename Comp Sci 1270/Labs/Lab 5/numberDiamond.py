# Gavin King    Lab 5   10-2-25
# This program will make a diamond made out o0f numbers where the widest layer counts up to the number provided

def numberDiamond(layers):
    for j in range(1, layers + 1):
        print(" " * (layers - j), end=" ")
        for i in range(1, j + 1):
             
             print(i, end=" ")
        print("")

#Bottom Half of Diamond
    for k in range(layers - 1 , 0, -1):
        print(" " * (layers - k), end=" ")
        for l in range(k , 0, -1):
            print(l, end=" ")
        print("")







def main():
    numberDiamond(int(input("How many layers for your diamond: ")))

if __name__ == "__main__":
    main()