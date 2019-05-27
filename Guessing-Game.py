import random
number = random.randint(1,20)
Guess = int(input("I'm thinking of a number from 1 to 20. What is it?"))
while Guess != number:
    if Guess < number:
        print("Your number was to low...")
    else:
        print("Your number was to high...")
    Guess = int(input("Please try again..."))
print("Congratulations! Correct answer!")



