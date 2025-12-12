# Gavin King    Lab 4   10-2-25
# This is a choose your own adventure where you must make your way out of a mysterious cave



def Main():
    print("You suddenly wake up with a splitting headache.")
    print("You find yourself in what appears to be a large cave, filled with bioluminescent fungi")
    print("In the faint glow of the mushrooms you see two different passages.")
    direction = input("Do you go in the [left] or [right] passage? ")
    if direction == "left":
        print("You go down the leftern passage, mushrooms lighting the way")
        print("As you go further you see a strange many limbed creature scuttle away in the opposite direction")
        print("You soon see what the strange animal was running away from, as a large bear sized monster starts charging at you")
        choice1 = input("Do you try to [dodge] the beast or [scare] it off: ")
        if choice1 == "scare":
            print("You made as loud a noise as you could.")
            print("It scared the beast and it ran down a previously unseen passage that leads deeper into the cave")
            print("Best not to follow in case it is still hungry")
            print("")
            print("You continue down the passage way, you see what appears to be a light")
            choice2 = input("Do you [investigate] or [not]? ")
            if choice2 == "investigate":
                print("You found a small crack to the surface!")
                print("After chiping at it with loose stones from the cave floor you widen it enough to escape")
                print("You've won!")
            else:
                print("In your hesitation, you hear another rumbling growl")
                print("All you can do is [run]")
                choice3 = input("RUN: ")
                if choice3 == "run":
                    print("you made it safely away from what ever was making that noise")
                    print("You even see a group of rescuers who have been searching for you")
                    print("You have won!")
                else:
                    print("You hesitated too long and now the beast is on top of you")
                    print("It opens it's many jawed mouth and bites down on your leg")
                    choice4 = input("[kick] it away or [accept] your fate? ")
                    if choice4 == "kick":
                        print("You manage to kick the beast off of you and find the damage it did to be minimal")
                        print("You scare the animal away by screaming at the top of your lungs")
                        print("The noise managed to both scare the animal off, and attracted a group of rescuers who have been searching for you")
                        print("You have won!")
                    else:
                        print("You accept your fate without challenge")
                        print("Your body will provide a boon of nutrients to this unique ecosystem at least...")
                        print("You have died")



        else:
            print("Your plan failed and the beast trampled you underfoot")
            print("You have died")
        



    elif direction == "right":
        print("You immediately fall into a deep pit full of water")
        print("It is freezing cold and you are not sure what to do")
        print("You died of hypothermia. Restart")



    else:
        print("You could not find your way and died")
        print("Start Again!")





if __name__ == "__main__":
    Main()