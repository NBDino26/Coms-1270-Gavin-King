# Gavin King    10-9-25     Lab #5

def multiplicationTable(lowNum, highNum):
    for j in range(1, highNum + 1):
        for i in range(highNum):
         print((lowNum + i) * j, end="  ".ljust(2))
        print("")
         
  
    



def main():
    multiplicationTable(int(input("Input the low number: ")), int(input("Input the high number: ")))

if __name__ == "__main__":
    main()