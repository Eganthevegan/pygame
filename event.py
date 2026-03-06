from tkinter import *

window = Tk()

def handle_keypress(event):
    """print the character associated to thhe key pressed"""
    print(event.char)

window.bind("<Key>", handle_keypress)

window.mainloop()