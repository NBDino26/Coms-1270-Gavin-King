# Gavin King    10-9-25     Lab 5
# THis program will make a right triangle with as many layers as the user specifies, with each layer being the same number

def sameNumberTriangle(times):
    for i in range(1, times + 1):
        print((str(i) + " ") * i)


def main():
    sameNumberTriangle(int(input("How many layers for the triangle: ")))

if __name__ == "__main__":
    main()