x = int(input("Choose a number"))
c = 0
while x != 1:
    if x % 2 == 0:
        x = x / 2
    else:
        x = (x * 3) + 1
    c = c + 1
    print("The number is",x)
print("GAME OVER")
print(c)