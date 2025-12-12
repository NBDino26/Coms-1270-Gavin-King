# Gavin King            12-5-25
# Assignment 6
#
# Candy Territory! Make your way to Candy Parliament to overthrow the Candy Autocrat!
# First one there leads the revolution!


import random

choice = ""
game = False
answer = False
roboPlayers = 0

board = [2, 1, 5, 4, 2, 3, 1, 3, 4, 2, 5, 1, 4, 3, 1, 2, 1, 5, 2, 3, 1, 4, 3, 3, 1, 5, 3, 3, 4, 5]

def robotPlayer(seed):
    pass



def mainLoop():
    while answer == False:
        choice = input("How many humans are playing? [1] [2] [3] [4]")
        if choice == "1":
            roboPlayers = 3
            answer = True
        elif choice == "2":
            roboPlayers = 2
            answer = True
        elif choice == "3":
            roboPlayers = 1
            answer = True
        elif choice == "4":
            roboPlayers = 0
            answer = True
        else:
            print("Please try a different response")
    








def main():
    print("Welcome to the Autonomous Candy Territory!")
    print("You are a revolutionary on your way to over throw Candy President for Life, Bub L Gum")
    print("You must compete against your fellow revolutionaries to see who leads the revolution")
    while game == False:
        choice = input("Type [R]ules, [S]tart, or [Q]uit")
        if choice == "R":
            print("")
        elif choice == "Q":
            print("Goodbye!")
            game = True
        elif choice == "S":
            game = True
            mainLoop()
        else:
            print("Please choose a different Answer")
            


if __name__ == "__main__":
    main()