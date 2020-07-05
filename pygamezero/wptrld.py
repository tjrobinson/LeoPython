from random import randint
gametype = input("What type of character would you like to be? Mage (m) or warrior (w)")
gamemode = input("Which mode would you like to play? normal (n), hard (h) or impossible (i)")
takeawayspeed = 3.0
counter = 0
counter2 = 0
def takeawayhealth():
    global lthigyhealth
    if gamemode=="n" and gametype=="w":
       takawayamount = randint(1, 3)
    elif gamemode=="h" and gametype=="w":
        takawayamount = randint(1, 6)
    elif gamemode=="i" and gametype=="w":
        takawayamount = randint(1, 10)
    elif gamemode=="n" and gametype=="m":
       takawayamount = randint(3, 6)
    elif gamemode=="h" and gametype=="m":
       takawayamount = randint(4, 8)
    elif gamemode=="i" and gametype=="m":
       takawayamount = randint(5, 10)
    lthigyhealth = lthigyhealth - takawayamount
def countup():
    global counter

    counter = counter + 1

def addcountertwo():
    global counter2
    counter2 = counter2 + 1

def addcounters():
    countup()
    addcountertwo()


if gamemode=="n" and gametype == "w":
    lthigy = Actor("lthigyattaking")
    colour = "green"
    WIDTH = 400
    HEIGHT = 400
    baddyname = "charcher"
    charcher = Actor("charcher")
    lthigyhealth = 50
    charcherhealth = 100
    moveamount = 4
    damagedone = 1
    lthigy.pos = 100, 100
    takeawayspeed = 3.0
    clock.schedule_interval(takeawayhealth, takeawayspeed)
elif gamemode == "h" and gametype == "w":
    lthigy = Actor("lthigyattaking")
    colour = "green"
    baddyname = "charcher"
    WIDTH = 400
    HEIGHT = 400
    lthigyhealth = 70
    charcherhealth = 140
    charcher = Actor("charcher")
    moveamount = 4
    damagedone = 1
    lthigy.pos = 100, 100
    takeawayspeed = 3.0
    clock.schedule_interval(takeawayhealth, takeawayspeed)
elif gamemode == "i" and gametype == "w":
    lthigy = Actor("lthigyattaking")
    colour = Actor("untitledback")
    baddyname = "Ogre"
    moveamount = 10
    lthigyhealth = 400
    charcherhealth = 1000
    charcher = Actor("download")
    WIDTH = 1000
    HEIGHT = 800
    damagedone = 5
    lthigy.pos = 100, 100
    takeawayspeed = 3.0


elif gamemode=="n" and gametype == "m":
    takeawayspeed = 3.0
    lthigy = Actor("mage")
    colour = "green"
    WIDTH = 400
    HEIGHT = 400
    baddyname = "charcher"
    charcher = Actor("charcher")
    lthigyhealth = 50
    charcherhealth = 1500
    moveamount = 15
    damagedone = 1
    lthigy.pos = 100, 100
    clock.schedule_interval(takeawayhealth, takeawayspeed)
elif gamemode == "h" and gametype == "m":
    lthigy = Actor("mage")
    colour = "green"
    baddyname = "charcher"
    WIDTH = 400
    HEIGHT = 400
    lthigyhealth = 70
    charcherhealth = 2000
    charcher = Actor("charcher")
    moveamount = 15
    damagedone = 2
    lthigy.pos = 100, 100
    clock.schedule_interval(takeawayhealth, takeawayspeed)
elif gamemode == "i" and gametype == "m":
    lthigy = Actor("mage")
    colour = "white"
    baddyname = "The Sun"
    moveamount = 15
    lthigyhealth = 400
    charcherhealth = 100000
    charcher = Actor("sun")
    WIDTH = 1000
    HEIGHT = 800
    damagedone = 10
    lthigy.pos = 100, 100







game_over = False
youhavewon = False



def place_charcher():
    global WIDTH
    charcher.x = randint(20, (WIDTH - 20))
    charcher.y = randint(20, (WIDTH - 20))



def update():
    global score
    global charcherhealth
    global lthigy
    global game_over
    global youhavewon
    global takeawayspeed
    global counter
    global counter2
    global lthigyhealth
    if keyboard.left:
        lthigy.x = lthigy.x - moveamount
    elif keyboard.right:
        lthigy.x = lthigy.x + moveamount
    elif keyboard.up:
        lthigy.y = lthigy.y - moveamount
    elif keyboard.down:
        lthigy.y = lthigy.y + moveamount
    charcher_collected = lthigy.colliderect(charcher)


    clock.schedule_interval(addcounters, 5.0)
    if gametype == "m":
        countup()
        if charcher_collected:
            takeawayspeed = takeawayspeed + 0.5
    if charcher_collected:
        place_charcher()
        if charcher_collected and gametype  == "w":
            charcherhealth = charcherhealth - damagedone
            attak = randint(1, 20)
            if attak == 1:
                lthigyhealth = lthigyhealth - 20
        elif gametype == "m":
            clock.schedule_interval(takeawayhealth, takeawayspeed)
        else:
            clock.schedule_interval(takeawayhealth, takeawayspeed)


    if counter > counter2 and game_over == False:
        charcherhealth = charcherhealth - damagedone
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