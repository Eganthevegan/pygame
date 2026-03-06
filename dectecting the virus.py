from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("200x200")

def msg():
    messagebox.showinfo("loading complete"," video downloaded.")

button = Button(root, text="load image", command=msg)
button.place(x=40, y=80)

root.mainloop()