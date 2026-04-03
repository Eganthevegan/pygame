import tkinter as tk
import random

def play_game(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"
    
    label.config(text=f"Computer chose: {computer_choice}\n{result}")

def click_rock():
    play_game("Rock")

def click_paper():
    play_game("Paper")

def click_scissors():
    play_game("Scissors")

root = tk.Tk()
root.title("Simple Game")
root.geometry("300x300")

label = tk.Label(root, text="Pick one to start!", pady=20)
label.pack()

tk.Button(root, text="Rock", width=15, command=click_rock).pack(pady=5)
tk.Button(root, text="Paper", width=15, command=click_paper).pack(pady=5)
tk.Button(root, text="Scissors", width=15, command=click_scissors).pack(pady=5)

root.mainloop()