import tkinter as tk
from tkinter import messagebox
import random

# Generate random number
secret_number = random.randint(1, 100)

# Variables
attempts = 0
best_score = None


# Function to check guess
def check_guess():
    global attempts, best_score, secret_number

    try:
        guess = int(entry.get())

        attempts += 1

        if guess < secret_number:
            result_label.config(
                text="Too Low! Try Again.",
                fg="blue"
            )

        elif guess > secret_number:
            result_label.config(
                text="Too High! Try Again.",
                fg="red"
            )

        else:

            # Update best score
            if best_score is None or attempts < best_score:
                best_score = attempts

            messagebox.showinfo(
                "Congratulations",
                f"🎉 Correct Guess!\n\n"
                f"Attempts: {attempts}\n"
                f"Best Score: {best_score}"
            )

            result_label.config(
                text="You guessed it correctly!",
                fg="green"
            )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid number"
        )


# Function to restart game
def restart_game():
    global secret_number, attempts

    secret_number = random.randint(1, 100)

    attempts = 0

    entry.delete(0, tk.END)

    result_label.config(text="")

    messagebox.showinfo(
        "Restart Game",
        "New Game Started!"
    )


# Main window
root = tk.Tk()

root.title("Number Guessing Game")

root.geometry("400x350")

root.config(bg="white")


# Title Label
title_label = tk.Label(
    root,
    text="🎯 Number Guessing Game",
    font=("Arial", 18, "bold"),
    bg="white",
    fg="black"
)

title_label.pack(pady=20)


# Instruction Label
instruction_label = tk.Label(
    root,
    text="Guess a number between 1 and 100",
    font=("Arial", 12),
    bg="white"
)

instruction_label.pack(pady=10)


# Entry Field
entry = tk.Entry(
    root,
    font=("Arial", 14)
)

entry.pack(pady=10)


# Guess Button
guess_button = tk.Button(
    root,
    text="Check Guess",
    font=("Arial", 12, "bold"),
    command=check_guess,
    bg="green",
    fg="white"
)

guess_button.pack(pady=10)


# Restart Button
restart_button = tk.Button(
    root,
    text="Play Again",
    font=("Arial", 12, "bold"),
    command=restart_game,
    bg="blue",
    fg="white"
)

restart_button.pack(pady=10)


# Result Label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    bg="white"
)

result_label.pack(pady=20)


# Run GUI
root.mainloop()