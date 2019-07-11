import random
xnumber = random.randint(0,20)
number = 0
def randomize():
        for x in range(0,xnumber):
                global number
                number1 = random.randint(0,2000)
                number2 = random.randint(500,700)
                number = number1 + number2
for x in range(0,10):
        randomize()
print(number)