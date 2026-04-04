#working aplha beta pruning
#Q1
ALPHA, BETA = float('-inf'), float('inf')
player, opponent = 'x', 'o'


def isMovesLeft(board):  #finding empty cells
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return True
    return False


def evaluate(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != '_':
            return 10 if board[row][0] == 'x' else -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '_':
            return 10 if board[0][col] == 'x' else -10

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_':
        return 10 if board[0][0] == 'x' else -10

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_':
        return 10 if board[0][2] == 'x' else -10

    return 0  # If draw or game still ongoing


def minimax(board, depth, isMax, alpha, beta):
    score = evaluate(board)

    if score == 10 or score == -10:
        return score

    if not isMovesLeft(board):
        return 0

    if depth == 0:
        return 0

    if isMax:
        best = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = player
                    best = max(best, minimax(board, depth - 1, not isMax, alpha, beta))
                    alpha = max(alpha, best)
                    board[i][j] = '_'
                    if beta <= alpha:
                        break
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = opponent
                    best = min(best, minimax(board, depth - 1, not isMax, alpha, beta))
                    beta = min(beta, best)
                    board[i][j] = '_'
                    if beta <= alpha:
                        break
        return best


def findBestMove(board):  #finding the best move for the current player
    bestVal = float('-inf')
    bestMove = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = player
                moveVal = minimax(board, 8, False, ALPHA, BETA)  # rescursion
                board[i][j] = '_'
                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal

    print("The value of the best Move is:", bestVal)
    return bestMove


def initialize_board():
    """ Initialize an empty Tic-Tac-Toe board. """
    return [['_', '_', '_'] for _ in range(3)]


def print_board(board):
    """ Print the current state of the board. """
    for row in board:
        print(' '.join(row))


def is_valid_move(board, row, col):
    """ Check if the given move is valid. """
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == '_'


# Initialize an empty board
board = initialize_board()
current_player = player

# Play until the game is over
while isMovesLeft(board):
    print_board(board)

    if current_player == player:
        print("Player 'x' turn")
        while True:
            try:
                row = int(input("Enter row (0, 1, 2): "))
                col = int(input("Enter column (0, 1, 2): "))
                if is_valid_move(board, row, col):
                    board[row][col] = player
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    else:
        print("Player 'o' turn")
        row, col = findBestMove(board)
        board[row][col] = opponent

    # Check if current player wins
    if evaluate(board) == 10:
        print_board(board)
        print("Player 'x' wins!")
        break
    elif evaluate(board) == -10:
        print_board(board)
        print("Player 'o' wins!")
        break


    current_player = opponent if current_player == player else player   #switching players

# If no one wins, it's a draw
if not isMovesLeft(board):
    print_board(board)
    print("It's a draw!")