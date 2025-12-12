# Gavin King    Lab 4   10-2-25

#This code will allow you in input a year and discover wether or not it is a leap year!

def findLeapYear(year):

    print("Find out wether a year is a leap year or not!")
   
    if year % 4 == 0:
        if year % 100 == 0:
           if year % 400 ==0:
            print("Yes")
           else:
            print("No")
        else:
            print("Yes") 
    else:
        print("No")


def Main():
  findLeapYear(int(input("Input your Year: ")))    

if __name__ == "__main__":
   Main()