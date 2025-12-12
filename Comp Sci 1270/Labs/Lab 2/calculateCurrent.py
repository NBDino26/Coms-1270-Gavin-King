voltage = input("Please input your voltage ")
resistence = input("Input your Resistence in Ohms ")
voltageInt = int(voltage)
resistenceInt = int(resistence)
current = voltageInt/resistenceInt
print("Your current is", current, "Amps")