apple = Actor("apple")
def draw():
    screen.clear()
    apple.draw()
def place_apple():
    apple.x = 300
    apple.y = 200