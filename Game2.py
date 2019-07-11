import tkinter
Games = 0
print("Please press the X in the code window.")
if Games > 0:
    print("To Join a current game press the button once.")
print("To start a new game press twice.")
window = tkinter.Tk()
clickcount = 0
button = tkinter.Button(window, text="", width=20)
button.pack(padx=5, pady=5)
currentgames = ""
def onclick(event):
    global currentgames
    global clickcount
    clickcount = clickcount + 1
    currentgames = True
    if clickcount > 0:
        canvas = tkinter.Canvas(window, width=1300, height=500, bg="black")
        canvas.pack()
if clickcount == 2:
    Games = Games + 1
button.bind("<ButtonRelease-1>", onclick)
savename = ""
def save_current_info(savename):
    def fib(n):
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a+b
    print()
    print(savename)
    fib(1000)
if currentgames == False:
    save_current_info()
window.mainloop()
