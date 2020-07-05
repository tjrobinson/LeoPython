import random
import time
from tkinter import messagebox
HEIGHT = 1000
WIDTH = 1000
cat1 = Actor("cat")
cat2 = Actor("cat2")
toy = Actor("toy")
toy.pos = 50, 50
cat1.pos = 50, 200
cat2.pos = 250, 300
game_over = False

def draw():
    toy.draw()
    cat1.draw()
    cat2.draw()
def update():
    global game_over
    screen.clear()
    if keyboard.left:
        toy.x = toy.x - 4
        clock.schedule(move_cat, 2.0)
    elif keyboard.right:
        toy.x = toy.x + 4
        clock.schedule(move_cat, 5.0)
    elif keyboard.up:
        toy.y = toy.y - 4
        clock.schedule(move_cat, 5.0)
    elif keyboard.down:
        toy.y = toy.y + 4
        clock.schedule(move_cat, 5.0)
    if toy.colliderect(cat1 or cat2):
        if random.randint(0, 2) == 1:
            #game_over = True
            pass
        else:
            print("You won the Tug!")
            if keyboard.left:
                toy.x = toy.x - 4
                clock.schedule(move_cat, 10.0)
            elif keyboard.right:
                toy.x = toy.x + 4
                clock.schedule(move_cat, 10.0)
            elif keyboard.up:
                toy.y = toy.y - 4
                clock.schedule(move_cat, 10.0)
            elif keyboard.down:
                toy.y = toy.y + 4
                clock.schedule(move_cat, 10.0)
    cat1.pos = toy.pos
    cat2.pos = toy.pos
    if game_over == True:
        question = messagebox.askyesno("Do you want to play again?")
def move_cat():
    cat1.x = toy.x - 300
    cat2.x = toy.x - 300
    cat1.x = toy.y - 300
    cat2.x = toy.y - 300
