import tkinter as tk

def calculate():
    p = float(entry_p.get())
    r = float(entry_r.get())
    t = float(entry_t.get())

    si = (p * r * t) / 100
    
    ci = p * (1 + r/100)**t - p

    label_result.config(text=f"SI: {si:.2f} | CI: {ci:.2f}")

app = tk.Tk()
app.title("Age Calculator App")
app.geometry("400x400")

tk.Label(app, text="Principal:").grid(row=0, column=0)
entry_p = tk.Entry(app)
entry_p.grid(row=0, column=1)

tk.Label(app, text="Rate (%):").grid(row=1, column=0)
entry_r = tk.Entry(app)
entry_r.grid(row=1, column=1)

tk.Label(app, text="Time (yrs):").grid(row=2, column=0)
entry_t = tk.Entry(app)
entry_t.grid(row=2, column=1)

btn = tk.Button(app, text="Calculate", command=calculate)
btn.grid(row=3, column=0, columnspan=2)

label_result = tk.Label(app, text="Results will show here")
label_result.grid(row=4, column=0, columnspan=2)

app.mainloop()