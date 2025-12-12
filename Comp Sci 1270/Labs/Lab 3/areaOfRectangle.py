# Lab 2     Gavin King
def areaOfRectangle(base, height):
    baseInt = int(base)
    heightInt = int(height)
    rectangleArea = baseInt * heightInt
    print ("Your area is", rectangleArea, "squared")
def main():
        val = input("Please enter your base: ")
        val2 = input("Please enter your height: ")
        answer = areaOfRectangle(val, val2)
        print("Your rectangle's area is", answer, "centimeters squared")
if __name__ == "__main__":
      main()