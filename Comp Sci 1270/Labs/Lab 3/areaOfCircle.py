import math
def areaOfCircle(radius):
    radiusInt = int(radius)
    area = math.pi * (radiusInt ** 2)
    print("Your circles area is", area,"squared")

def main():
        val = input("Please enter your radius")
        answer = areaOfCircle(val)
        print("Your circle's area is", answer)
if __name__ == "__main__":
      main()