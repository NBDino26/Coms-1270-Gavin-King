# Gavin King    Lab 5   10-2-25
# This code will draw a right triangle made out of * symbols in as many rows as the user specifies

def rightTriangleStars(times):
    for i in range(1, times + 1):
        print("* " * i)


def main():
    rightTriangleStars(int(input("How many layers for the triangle: ")))

if __name__ == "__main__":
    main()