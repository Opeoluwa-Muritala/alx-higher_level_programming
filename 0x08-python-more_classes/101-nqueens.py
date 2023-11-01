#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at a given position on the board."""
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_nqueens(n):
    """Solve the N-queens problem for a given board size."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    solutions = []

    def solve(row):
        if row == n:
            solutions.append([''.join(row) for row in board])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 'Q'
                solve(row + 1)
                board[row][col] = ' '

    solve(0)
    return solutions

def main():
    """Main entry point for the N-Queens solver."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        for row in solution:
            print(row)
        print()

if __name__ == "__main__":
    main()

