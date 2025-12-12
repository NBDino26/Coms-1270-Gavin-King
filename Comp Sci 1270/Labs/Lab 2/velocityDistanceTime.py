acceleration = input("Input accerlation in m/s")
time = input("input length of time in seconds")
intialVelocity = input("input initial velocity")

accerlerationInt = int(acceleration)
timeInt = int(time)
intialVelocityInt = int(intialVelocity)

finalVelocity = intialVelocityInt + (accerlerationInt * timeInt)
print(finalVelocity)