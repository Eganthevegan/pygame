import tkinter as tk

def get_age():
    name = name_box.get()
    birth_year = int(year_box.get())
    
    age = 2026 - birth_year
    
    message = "Hi " + name + "! You are " + str(age) + " years old."
    
    result.config(text=message)

app = tk.Tk()
app.title("Age Calculator App")
app.geometry("400x400")


tk.Label(app, text="Name:").grid(row=0, column=0)
name_box = tk.Entry(app)
name_box.grid(row=0, column=1)

tk.Label(app, text="Day:").grid(row=1, column=0)
day_box = tk.Entry(app)
day_box.grid(row=1, column=1)

tk.Label(app, text="Month:").grid(row=2, column=0)
month_box = tk.Entry(app)
month_box.grid(row=2, column=1)

tk.Label(app, text="Year:").grid(row=3, column=0)
year_box = tk.Entry(app)
year_box.grid(row=3, column=1)

tk.Button(app, text="Calculate", command=get_age).grid(row=4, column=0, columnspan=2)

result = tk.Label(app, text="")
result.grid(row=5, column=0, columnspan=2)

app.mainloop()