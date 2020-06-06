from random import randint

gamemode = input("Which mode would you like to play? normal (n), hard (h) or impossible (i)")

if gamemode=="n":
    colour = "green"
    WIDTH = 400
    HEIGHT = 400
    baddyname = "charcher"
    charcher = Actor("charcher")
    lthigyhealth = 50
    charcherhealth = 100
    moveamount = 4
    damagedone = 1
elif gamemode=="h":
    colour = "green"
    baddyname = "charcher"
    WIDTH = 400
    HEIGHT = 400
    lthigyhealth = 70
    charcherhealth = 140
    charcher = Actor("charcher")
    moveamount = 4
    damagedone = 1
elif gamemode=="i":
    colour = "white"
    baddyname = "The Moon"
    moveamount = 10
    lthigyhealth = 400
    charcherhealth = 1000
    charcher = Actor("download")
    WIDTH = 1000
    HEIGHT = 800
    damagedone = 5


game_over = False
youhavewon = False

lthigy = Actor("lthigy")
lthigy.pos = 100, 100


def place_charcher():
    charcher.x = randint(20, (WIDTH - 20))
    charcher.y = randint(20, (WIDTH - 20))

def takeawayhealth():
    global lthigyhealth
    if gamemode=="n":
       takawayamount = randint(1, 3)
    elif gamemode=="h":
        takawayamount = randint(1, 6)
    elif gamemode=="i":
        takawayamount = randint(1, 10)
    lthigyhealth = lthigyhealth - takawayamount

def update():
    global score
    global charcherhealth
    global lthigy
    global game_over
    global youhavewon
    if keyboard.left:
        lthigy.x = lthigy.x - moveamount
    elif keyboard.right:
        lthigy.x = lthigy.x + moveamount
    elif keyboard.up:
        lthigy.y = lthigy.y - moveamount
    elif keyboard.down:
        lthigy.y = lthigy.y + moveamount
    charcher_collected = lthigy.colliderect(charcher)
    if charcher_collected:
        lthigy = Actor("lthigyattaking")
        charcherhealth = charcherhealth - damagedone
        place_charcher()
    else:
        thigy = Actor("lthigy")
    if lthigyhealth <= 0:
        game_over = True
    elif charcherhealth <= 0:
        youhavewon = True

def draw():
    screen.fill(colour)
    lthigy.draw()
    charcher.draw()

    if game_over:
        screen.fill("pink")
        screen.draw.text("You died... the " + str(baddyname) + " still had " + str(charcherhealth) + " health!", topleft=(10, 10), fontsize=30, color="black")
    elif youhavewon:
        screen.fill("pink")
        screen.draw.text("You won!!! You still had " + str(lthigyhealth) + " health!", topleft=(10, 10), fontsize=30, color="black")
    else:
        screen.draw.text("Lthigy: " + str(lthigyhealth) + " " + str(baddyname) + ": " + str(charcherhealth), topleft=(10, 10), fontsize=30, color="black")

place_charcher()

clock.schedule_interval(takeawayhealth, 3.0)