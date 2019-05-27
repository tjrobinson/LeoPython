import tkinter
window = tkinter.Tk()
button = tkinter.Button(window, text="Do not press this button.", width=40)
button.pack(padx=10, pady=10)
clickcount = 0
def onClick(event):
    global clickcount
    clickcount = clickcount + 1
    if clickcount == 1:
        button.configure(text="Seriously? Do. Not. Press. It.")
    elif clickcount == 2:
        button.configure(text="Gah! next time, no more button.")
    else:
        button.pack_forget()
button.bind("<ButtonRelease-1>", onClick)
window.mainloop()
