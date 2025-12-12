# Gavin King            11-5-2025
# Lab 8
# This program will

assignmentsCompleted = []
totalScoreList = []
idNumber = []
idNumbers = []

grades = [["Student ID", "Name", "Total Scores", "Sum of All Scores", "Score Average"]]

def textToFile(string):
    file = open(string, "r")
    text = file.read()
    return text

def isolateIDNumbers(file):
    idNumber = ""
    for i in file:
        if i.isdigit():
            idNumber = idNumber + i
        elif i == " ":
            idNumber = idNumber + i
    splitList = idNumber.split()
    for i in range(len(splitList)):
        int(splitList[i])
    return splitList

def numberOfGrades(id, scores):
    assignments = 0
    splitList = scores.split()
    
    
    for i in splitList:
       
        if i == str(id)+",":
            assignments = assignments + 1
    assignmentsCompleted.append(assignments)

def totalScore(scores, assignments):
    totalScore = 0
    splitList = scores.split(",")
    print(splitList)
    numberAssigned = 0

    while numberAssigned < 5:
        num = 5
        for i in splitList:
            if i == splitList[num]:
                totalScore = totalScore + int(i)
                print(totalScore)
                
                num = num + 3
            numberAssigned = numberAssigned + 1   
       
        print(numberAssigned)

    totalScoreList.append(totalScore)



def averageScore():
    pass


def fileCreation(text, title):
    make = open("grades" + ".txt", "x")
    make.write(text)






if __name__ == "__main__":
    fileNameOne = "students.txt"
    fileNameTwo = "scores.txt"

    fileOneString = textToFile(fileNameOne)
    idStrings = isolateIDNumbers(fileOneString)
   
    fileTwoString = textToFile(fileNameTwo)

    for i in range(len(idStrings)):
        numberOfGrades(idStrings[i], fileTwoString)

    totalScore( fileTwoString, assignmentsCompleted[0])

    print(assignmentsCompleted)
    print(totalScoreList)




    











