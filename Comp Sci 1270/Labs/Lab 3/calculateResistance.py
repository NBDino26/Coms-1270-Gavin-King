def calculateResistance(voltage, current):
    voltageInt = int(voltage)
    currentInt = int(current)
    resistance = voltageInt/currentInt
    print("Your resistance is",resistance,"ohms")