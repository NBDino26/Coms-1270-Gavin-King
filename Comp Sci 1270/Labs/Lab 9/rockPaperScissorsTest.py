# Gavin King        11/20/2025
# Lab 9
# This program is a set of tests for the rock paper scissors program

from rockPaperScissors import roundWinner
from rockPaperScissors import computerTurn

def test_computer():
    computerTurn()

def test_win():
    roundWinner("paper", "paper")
    roundWinner("paper", "rock")








def main():
    pass


if __name__ == "__main__":
    main()