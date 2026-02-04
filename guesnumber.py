import random
import tkinter as tk
from tkinter import messagebox

def start_new_game():
    global secret_number, tries
    secret_number = random.randint(1, 100)
    tries = 0
    result_label.config(text="")
    score_label.config(text="Score: 0")
    entry.delete(0, tk.END)

def check_guess():
    global tries
    guess = entry.get()

    if not guess.isdigit():
        messagebox.showwarning("Error", "Please enter a number")
        return

    guess = int(guess)
    tries += 1
    score = max_tries - tries + 1
    score_label.config(text=f"Score: {max(score, 0)}")

    if guess < secret_number:
        result_label.config(text="Too low ❄️")
    elif guess > secret_number:
        result_label.config(text="Too high 🔥")
    else:
        messagebox.showinfo(
            "You Win 🎉",
            f"You guessed it in {tries} tries!\nScore: {score}"
        )

    if tries >= max_tries and guess != secret_number:
        messagebox.showerror(
            "Game Over ❌",
            f"Out of tries!\nNumber was {secret_number}"
        )

# Game setup
max_tries = 7
secret_number = random.randint(1, 100)
tries = 0

# Window
window = tk.Tk()
window.title("Guess the Number Game")
window.geometry("360x300")

tk.Label(window, text="Guess a number (1–100)", font=("Arial", 14)).pack(pady=10)

entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=5)

tk.Button(window, text="Check Guess", command=check_guess).pack(pady=8)
tk.Button(window, text="Restart Game 🔁", command=start_new_game).pack(pady=5)

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=5)

score_label = tk.Label(window, text="Score: 0", font=("Arial", 12))
score_label.pack(pady=5)

window.mainloop()
