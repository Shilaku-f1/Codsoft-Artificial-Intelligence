import tkinter as tk
from tkinter import messagebox

import random  # For adding randomness to the AI's decisions


# Function to initialize the game board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]


# Function to check for a winner
def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0], [(i, 0), (i, 1), (i, 2)]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i], [(0, i), (1, i), (2, i)]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0], [(0, 0), (1, 1), (2, 2)]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2], [(0, 2), (1, 1), (2, 0)]
    
    return None, []


# Function to check if the board is full (draw)
def is_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True


# Function for the AI's move using Minimax
def minimax(board, depth, is_maximizing):
    winner, _ = check_winner(board)
    if winner == 'O':
        return 10 - depth  # AI wins
    if winner == 'X':
        return depth - 10  # Player wins
    if is_draw(board):
        return 0  # Draw

    if is_maximizing:
        best_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[row][col] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[row][col] = ' '
                    best_score = min(score, best_score)
        return best_score


# Function to determine the best move for the AI
def ai_move():
    # Introduce randomness for reduced difficulty
    if random.random() < 0.5:  # 50% chance the AI will make a random move
        available_moves = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
        if available_moves:
            row, col = random.choice(available_moves)
            board[row][col] = 'O'
            buttons[row][col].config(text='O', state=tk.DISABLED, disabledforeground="red")
            return

    # Otherwise, play the optimal move using Minimax
    best_score = float('-inf')
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                score = minimax(board, 0, False)
                board[row][col] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    
    if best_move:
        row, col = best_move
        board[row][col] = 'O'
        buttons[row][col].config(text='O', state=tk.DISABLED, disabledforeground="red")


# Function for when a button is clicked
def button_click(row, col):
    global player_score, ai_score

    if board[row][col] == ' ':
        # Player move
        board[row][col] = 'X'
        buttons[row][col].config(text='X', state=tk.DISABLED, disabledforeground="blue")
        
        # Check for winner
        winner, combo = check_winner(board)
        if winner:
            if winner == 'X':
                player_score += 1
                highlight_winner(combo, "green")
                update_scoreboard()
                messagebox.showinfo("Game Over", "You Win!")
            else:
                ai_score += 1
                highlight_winner(combo, "red")
                update_scoreboard()
                messagebox.showinfo("Game Over", "You Lose!")
            reset_board()
            return
        
        if is_draw(board):
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
            return
        
        # AI move
        ai_move()
        
        # Check for winner after AI move
        winner, combo = check_winner(board)
        if winner:
            if winner == 'X':
                player_score += 1
                highlight_winner(combo, "green")
                update_scoreboard()
                messagebox.showinfo("Game Over", "You Win!")
            else:
                ai_score += 1
                highlight_winner(combo, "red")
                update_scoreboard()
                messagebox.showinfo("Game Over", "You Lose!")
            reset_board()
            return
        
        if is_draw(board):
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()


# Function to highlight the winning combination
def highlight_winner(combo, color):
    for row, col in combo:
        buttons[row][col].config(bg=color)


# Function to reset the board
def reset_board():
    global board
    board = initialize_board()
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text='', state=tk.NORMAL, bg="SystemButtonFace")


# Function to update the scoreboard
def update_scoreboard():
    score_label.config(text=f"You: {player_score} | AI: {ai_score}")


# Create the Tkinter window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Set the window background color
root.configure(bg="lightblue")

# Initialize the game board and scores
board = initialize_board()
player_score = 0
ai_score = 0

# Create the scoreboard
score_label = tk.Label(root, text=f"Play against AI        You: {player_score} | AI: {ai_score}", font=('Arial', 14), bg="lightblue")
score_label.grid(row=0, column=0, columnspan=3)

# Create a 3x3 grid of buttons
buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text='', font=('Arial', 24), width=5, height=2,
                                      bg="white", fg="black",
                                      command=lambda r=row, c=col: button_click(r, c))
        buttons[row][col].grid(row=row+1, column=col, padx=5, pady=5)

# Add Reset and Exit buttons
reset_button = tk.Button(root, text="Reset", font=('Arial', 14), command=reset_board, bg="orange", fg="white")
reset_button.grid(row=4, column=0, columnspan=1)

exit_button = tk.Button(root, text="Exit", font=('Arial', 14), command=root.quit, bg="red", fg="white")
exit_button.grid(row=4, column=2, columnspan=1)

# Start the Tkinter main loop
root.mainloop()
