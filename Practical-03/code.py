import random

def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], end=" | ")
        print("\n-------------")

def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def make_computer_move(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                if check_win(board, "O"):
                    return

                # Undo the move
                board[i][j] = " "

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                if check_win(board, "X"):
                    board[i][j] = "O"
                    return

                # Undo the move
                board[i][j] = " "

    while True:
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        if board[i][j] == " ":
            board[i][j] = "O"
            return

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]

    current_player = "X"

    while True:
        print_board(board)

        if current_player == "X":
            while True:
                row = int(input("Enter the row (0-2): "))
                col = int(input("Enter the column (0-2): "))
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Invalid move. Try again.")
        else:
            make_computer_move(board)

        if check_win(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break

        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            print_board(board)
            print("It's a draw")
            break

        current_player = "O" if current_player == "X" else "X"

play_game()