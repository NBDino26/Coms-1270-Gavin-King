# Gavin King            10-28-25
# Lab Week 7

import random

randomList=[]
sum = 0


def generateInput():
    for i in range(random.randint(200, 500)):
        randomList.append(random.randint(1, 2000))

def findMean(sum):
    # https://en.wikipedia.org/wiki/Mean
    # The mean is the sum of all numbers in the list, divided by the number of numbers in the list
    for i in randomList:
        sum = sum + randomList.index(i)
    mean = sum/len(randomList)
    return(mean)
    

def findMedian():
    randomList.sort 
    if len(randomList) % 2 == 0:
         limit = len(randomList)/2
         median = (randomList[limit] + randomList[limit + 1])/2
    else:
         limit = len(randomList)//2
         median = randomList[limit]
    return(median)




def main():
    generateInput()
    meanValue = findMean(0)
    medianValue = findMedian()
    print("The mean is ", meanValue)
    print("The median is ", medianValue)



if __name__ == "__main__":
    main()