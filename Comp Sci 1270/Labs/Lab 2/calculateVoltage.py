current = input("Input you Current in Amperage")
resistence = input("Input your Resistence in Ohms")
currentInt = int(current)
resistenceInt = int(resistence)

voltage = currentInt * resistenceInt
print(voltage, "is your voltage")