#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Function to check if the game is over
def is_game_over(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True, board[i][0]  # Row win
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True, board[0][i]  # Column win
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True, board[0][0]  # Diagonal win
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True, board[0][2]  # Diagonal win

    # Check for a draw
    if all(board[i][j] != " " for i in range(3) for j in range(3)):
        return True, "Draw"

    return False, None  # Game is not over

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    # Check if the game is over
    game_over, winner = is_game_over(board)
    if game_over:
        if winner == "X":
            return 1
        elif winner == "O":
            return -1
        else:
            return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "  # Undo the move
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "  # Undo the move
                    best_score = min(score, best_score)
        return best_score

# Function to find the best move for the AI (X)
def find_best_move(board):
    best_score = -float("inf")
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                score = minimax(board, 0, False)
                board[i][j] = " "  # Undo the move
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Main function to play Tic-Tac-Toe
def play_tic_tac_toe():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Initial Board:")
    print_board(board)

    while True:
        # AI's turn (X)
        print("\nAI's Turn (X):")
        move = find_best_move(board)
        board[move[0]][move[1]] = "X"
        print_board(board)

        # Check if the game is over
        game_over, winner = is_game_over(board)
        if game_over:
            if winner == "X":
                print("AI (X) wins!")
            elif winner == "O":
                print("Player (O) wins!")
            else:
                print("It's a draw!")
            break

        # Player's turn (O)
        print("\nPlayer's Turn (O):")
        while True:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            if board[row][col] == " ":
                board[row][col] = "O"
                break
            else:
                print("Invalid move. Try again.")
        print_board(board)

        # Check if the game is over
        game_over, winner = is_game_over(board)
        if game_over:
            if winner == "X":
                print("AI (X) wins!")
            elif winner == "O":
                print("Player (O) wins!")
            else:
                print("It's a draw!")
            break

# Run the game
play_tic_tac_toe()


# In[ ]:




