
intialVelocity = input("input initial velocity")
def velocityDistanceTime(acceleration,time,initialVelocity):
    accerlerationInt = int(acceleration)
    timeInt = int(time)
    intialVelocityInt = int(intialVelocity)

    finalVelocity = intialVelocityInt + (accerlerationInt * timeInt)
    print(finalVelocity)