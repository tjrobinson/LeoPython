import random
exitchoice = "Nothing"
while exitchoice != "EXIT":
    print("You are in a dark room in a myserious castle")
    print("In front of you are 3 doors. you must chose one")
    playerchoice = input("Chose 1,2 or 3")
    if playerchoice == "1":
        print("You find yourself in a room full of treasure you're rich!")
        print("GAME OVER, YOU WIN!")
    elif playerchoice == "2":
        print("The door opens and an angry ogre hits you with his club")
        print("GAME OVER, YOU LOSE!")
    elif playerchoice == "3":
        print("You go into the room and find a sleeping dragon")
        print("You can either,")
        print("(1)Try to steal some of the dragons gold.")
        print("(2)Try to sneak aroud the dragon to the exit.")
        playerchoicedragon = input("choose 1 or 2.")
        if playerchoicedragon == "1":
            print("The dragon wakes up and eats you,")
            print("GAME OVER, YOU LOSE!")
        elif playerchoicedragon == "2":
            print("You sneak around the dragon and escape the castle, blinking in the sunshine")
            print("GAME OVER, YOU WIN")
        else:
            print("Sorry, you didn't enter 1 or 2!")
    else:
        print("Sorry, you didn't enter 1,2 or 3")
    print("Run the program again to have another go.")
    exitchoice = input("Press return to play again, or type EXIT to leave")
