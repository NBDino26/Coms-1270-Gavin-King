def calculateCurrent(voltage, resistence):
    voltageInt = int(voltage)
    resistenceInt = int(resistence)
    current = voltageInt/resistenceInt
    

def main():
        val = input("Please enter your voltage: ")
        val2 = input("Please enter your resistance: ")
        answer = calculateCurrent(val, val2)
        print("Your current is", answer, "Amps")
if __name__ == "__main__":
      main()