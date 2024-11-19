def print_board(board):
    """Print the chessboard with queens."""
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()
def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i][col]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False
    return True
def solve_n_queens(board, row, n):
    """Use backtracking to solve the N-Queen problem."""
    if row == n:
        print_board(board)
        return True  
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1 
            if solve_n_queens(board, row + 1, n):
                return True  
            board[row][col] = 0 
    return False
def n_queens(n):
    """Initialize the board and solve the N-Queen problem."""
    board = [[0] * n for _ in range(n)]
    if not solve_n_queens(board, 0, n):
        print("No solution exists.")
    else:
        print("Solution found!")
n_queens(8)
