from random import randint
import time
answer = 0
numberone = 0
numbertwo = 0
count = 26
realanswer = 0
answer = 0
order = 0
score = 0

def randomize():
    global numberone
    global numbertwo
    global realanswer
    global order
    numberone = randint(1, 12)
    numbertwo = randint(1, 12)
    realanswer = numberone * numbertwo
    test = randint(1, 2)
    if test == 1:
        order = 12
    else:
        order = 21


while count > 1:
    count = count - 1
    if count == 25:
        print("Loading...")
    time.sleep(3.0)
    randomize()
    if numberone == 1:
        randomize()
    if numbertwo == 1:
        randomize()
    if order == 12:
        answer = int(input(str(numberone) + " x " + str(numbertwo) + " = "))
        if answer == realanswer:
            print("Well Done!")
            score = score + 1
            if count > 1:
                print("Loading... " + str(count - 1) + " To go!")
        else:
            print("Uh Oh...")
            if count > 1:
                print("Loading... " + str(count - 1) + " To go!")
    else:
        answer = int(input(str(numbertwo) + " x " + str(numberone) + " = "))
        if answer == realanswer:
            print("Well Done")
            score = score + 1
            if count > 1:
                print("Loading... " + str(count - 1) + " To go!")
        else:
            print("Uh Oh...")
            if count > 1:
                print("Loading... " + str(count - 1) + " To go!")
print("Your score was " + str(score) + " !")





