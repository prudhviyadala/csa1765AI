def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(all(cell != " " for cell in row) for row in board)

def get_player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                return row, col
            else:
                print("That cell is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 1 and 9.")

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    print("Welcome to Tic Tac Toe!")
    print("Player 1: X | Player 2: O")
    print("The board positions are as follows:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")
    print("-" * 20)
    while True:
        print_board(board)
        row, col = get_player_move(board, players[current_player])
        board[row][col] = players[current_player]

        if is_winner(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 1 - current_player  # Switch player

if __name__ == "__main__":
    play_tic_tac_toe()
