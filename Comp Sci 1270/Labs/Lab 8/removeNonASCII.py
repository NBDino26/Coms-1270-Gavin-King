# Gavin King            11-5-2025
# Lab 8
# This program will remove non ASCII characters from text




def textToVariable(string):
    file = open(string, "r")
    text = file.read()
    return text

def removeNonASCII(file):
    clean = ""
    for i in range(len(file)):
        if ord(file[i]) <= 128:
            clean = clean + file[i]
    return clean

def cleanFileCreation(text, title):
    make = open(title+"_clean"+".txt", "x")
    make.write(text)






if __name__ == "__main__":
    fileName = input("please input the name of a text file, no .txt required: ")
    middle = fileName +".txt"
    fileContents = textToVariable(middle)
    cleanText = removeNonASCII(fileContents)
    cleanFileCreation(cleanText, fileName)

