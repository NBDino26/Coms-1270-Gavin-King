voltage = input("Please input your voltage ")
current = input("Please input your current in Amps ")
voltageInt = int(voltage)
currentInt = int(current)
resistance = voltageInt/currentInt
print("Your resistance is",resistance,"ohms")