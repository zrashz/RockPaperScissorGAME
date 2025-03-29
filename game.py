import tkinter as tk
import random

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Function to play the game
def play(choice):
    computer_choice = random.choice(choices)
    result = determine_winner(choice, computer_choice)
    
    player_label.config(text=f"Player: {choice}")
    computer_label.config(text=f"Computer: {computer_choice}")
    result_label.config(text=f"Result: {result}")

# Function to determine winner
def determine_winner(player, computer):
    if player == computer:
        return "It's a Draw!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "You Win!"
    else:
        return "Computer Wins!"

# Function to reset game
def reset():
    player_label.config(text="Player: ")
    computer_label.config(text="Computer: ")
    result_label.config(text="Result: ")

# Labels
player_label = tk.Label(root, text="Player: ", font=("Arial", 14))
player_label.pack()

computer_label = tk.Label(root, text="Computer: ", font=("Arial", 14))
computer_label.pack()

result_label = tk.Label(root, text="Result: ", font=("Arial", 16, "bold"))
result_label.pack()

# Buttons for Rock, Paper, Scissors
for choice in choices:
    btn = tk.Button(root, text=choice, font=("Arial", 12), width=10, command=lambda c=choice: play(c))
    btn.pack(pady=5)

# Reset Button
reset_btn = tk.Button(root, text="Reset", font=("Arial", 12), width=10, command=reset)
reset_btn.pack(pady=10)

# Run the GUI
root.mainloop()
