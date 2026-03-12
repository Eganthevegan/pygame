import tkinter as tk

def convert():
    res = float(e.get()) * 2.54
    lbl.config(text=str(res) + " cm")

root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")

e = tk.Entry(root)
e.pack(pady=20)

btn = tk.Button(root, text="Convert", command=convert)
btn.pack(pady=10)

lbl = tk.Label(root, text="Result will appear here")
lbl.pack(pady=20)

root.mainloop()