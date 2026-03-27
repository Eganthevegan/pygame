import tkinter as tk

def show_strength():
    password = entry.get()
    n = len(password)
    
    if n <= 5:
        result.config(text="Weak", fg="Red")
    elif 6 <= n <= 8:
        result.config(text="Medium", fg="Yellow")
    elif n > 12:
        result.config(text="Very Strong", fg="Dark Green")
    elif n > 8:
        result.config(text="Strong", fg="Light Green")

root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")

tk.Label(root, text="Enter Password:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)

tk.Button(root, text="Check", command=show_strength).pack(pady=10)

result = tk.Label(root, text="", font=("Arial", 14, "bold"))
result.pack(pady=20)

root.mainloop()