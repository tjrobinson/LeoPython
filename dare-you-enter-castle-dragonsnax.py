print("you are in a dark room in a myserious castle")
print("in front of you are 4 doors. you must chose one")
playerchoice = input("chose 1,2 or 3")
if playerchoice == "1":
    print("you find yourself in a room full of treasure your rich!")
    print("GAME OVER, YOU WIN!")
elif playerchoice == "2":
    print("the door opens and an angry ogre hits you with his club")
    print("GAME OVER, YOU LOSE!")
elif playerchoice == "3":
    print("You go into the room and find a sleeping dragon")
    print("The dragon wakes up and eats you.You are delicious")
    print("GAME OVER, YOU LOSE!") 
else:
    print("Sorry, you didn't enter 1,2 or 3")
print("Run the program again to have another go.")

