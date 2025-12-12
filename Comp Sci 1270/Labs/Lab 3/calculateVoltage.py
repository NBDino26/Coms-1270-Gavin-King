def calculateVoltage(current, resistence):
    currentInt = int(current)
    resistenceInt = int(resistence)

    voltage = currentInt * resistenceInt
    print(voltage, "is your voltage")