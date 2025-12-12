# Gavin King        11/20/2025
# Lab 9
# This program is a simple game of rock paper scissors!

import random

playerMove = "0"

computerMove = "0"


def startGame():
    working = True
    rounds = 1
    print("Welcome to Rock Paper Scissors!")

    while working == True:
    
        rounds = input("Please input an odd number of rounds to play: ")
        if int(rounds) % 2 == 0:
            print("Please enter an odd number of rounds!")
        else:
            working = False
    rounds = int(rounds)
    return rounds

def computerTurn():
    choice = ""
    number = random.randrange(1, 3, 1)
    
    if number == 1:
        choice = "paper"
    elif number == 2:
        choice = "rock"
    else:
        choice = "scissors"

    return choice




def roundWinner(player, computer):
    winner = ""

    if player == "paper":
        if computer == "paper":
            winner = "Neither"
        elif computer == "scissors":
            winner = "Computer"
        elif computer == "rock":
            winner = "Player"
    
    elif player == "rock":
        if computer == "rock":
            winner = "Neither"
        elif computer == "paper":
            winner = "Computer"
        elif computer == "scissors":
            winner = "Player"    

    elif player == "scissors":
        if computer == "scissors":
            winner = "Neither"
        elif computer == "rock":
            winner = "Computer"
        elif computer == "paper":
            winner = "Player"   
    


    return winner



def playingGame(rounds):
    
    roundsPlayed = 0
    roundsWonPlayer = 0
    roundsWonComputer = 0

    roundsNeeded = (rounds // 2) + 1

    winner = ""

    for i in rounds:
        playersChoice = input("Choose [rock], [paper], or [scissors]")
        computersChoice = computerTurn()

        round = roundWinner(playersChoice, computersChoice)
        
        if round == "Player":
            roundsWonPlayer += 1
            roundsPlayed += 1
        elif round == "Computer":
            roundsWonComputer += 1
            roundsPlayed += 1
        
        if roundsWonPlayer == roundsNeeded:
            winner = "The Human"
            break
        elif roundsWonComputer == roundsNeeded:
            winner = "The Computer"
            break
    
    return winner







def main():
    rounds = startGame()
    gameWinner = playingGame(rounds)
    print(gameWinner, "is the winner!")


if __name__ == "__main__":
    main()