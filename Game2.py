def playgame():
    import tkinter
    from tkinter import messagebox
    message = tkinter.messagebox.askyesno(message="Do you want to play Unknowns?")
    message2 = tkinter.messagebox.askyesno(message="Do you want to play Laser Wars?")
    window = tkinter.Tk()
    def createlaser():
        square = tkinter.Label(window, text = "    ", bg = "red")
        square.grid()
    if message == "yes":
        Games = 0
        if Games > 0:
            print("To Join a current game press the button once.")
        print("To start a new game press twice.")
        clickcount = 0
        button = tkinter.Button(window, text="", width=20)
        button.pack(padx=5, pady=5)
        currentgames = ""
        def onclick1(event):
            global currentgames
            global Games
            global clickcount
            clickcount = clickcount + 1
            currentgames = True
            if clickcount == 1:
                canvas1 = tkinter.Canvas(window, width=1300, height=500, bg="black")
                canvas1.pack()
            if clickcount == 2:
                Games = Games + 1
                savename = ""
                canvas2 = tkinter.Canvas(window, width=1300, height=500, bg="black")
                canvas2.pack()
        button.bind("<ButtonRelease-1>", onclick1)
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
        lasers, paintsplats = 0
    def onclick(square,item,game,gametype,window):
        global lasers, paintsplats
        global deaths
        global scores
        if Choice == "laser":
            createlaser()
playgame()
