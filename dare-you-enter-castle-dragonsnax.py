
exitchoice = "Nothing"
while exitchoice != "EXIT":
    print("Dare You Enter Castle Dragonsnax")
    print("          The Game")
    print("Type yes to play")
    if playchoice == "yes": 

    print("You are in a dark room in a myserious castle")
    print("In front of you are 4 doors. you must chose one")
    playerchoice = input("Chose 1,2,3 or 4")
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
    elif playerchoice == "4":
        print("You enter a room with a sphinx.")
        print("It asks you what number it is thinking of, between one and 5.")
        playerchoicesphinx = int(input("What number do you choose?"))
        import random
        if playerchoicesphinx == random.randint(1,5):
            print("The sphinx hisses in disappointment. You guessed correctly.")
            print("She must let you go.")
            print("GAME OVER, YOU WIN!")
        else:
            print("The sphinx tells you that your guess is incorrect.")
            print("You are her prisoner forever")
            print("GAME OVER, YOU LOSE!")
    else:
        print("Sorry, you didn't enter 1,2,3 or 4")
    print("Run the program again to have another go.")
    exitchoice = input("Press return to play again, or type EXIT to leave")
    if exitchoice == "EXIT":
        exitchoice2 = input("Are you sure you want to leave? Type 'EXIT' to leave or press enter to play again.")
        if exitchoice2 == "EXIT":
            print("Quitting...")
            print("Done!")
