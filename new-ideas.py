import tkinter
window = tkinter.Tk()

clickcount = 0

def onClick(event):
    global clickcount
    clickcount = clickcount + 1
    if clickcount == 1:
        button2 = tkinter.Button(window, text="OK, so" "is your favorite colour")

button1 = tkinter.Button(window, text="What is your favorite colour? choose red(1), green(2), orange(3) or yellow(4)", width=40)
button1.pack(padx=10, pady=10)
colour1 = tkinter.Button(window, text="1", width=40)
colour1.pack(padx=10, pady=10)
colour1.bind("<ButtonRelease-1>", onClick)

