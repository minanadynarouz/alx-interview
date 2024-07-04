#!/usr/bin/python3
import sys

"""N-queens problem"""


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)


def is_safe(board, row, col):
    """Check if the queen is safe in the given row and column"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col, solutions):
    """Solve the N-Queens problem using backtracking"""
    if col >= len(board):
        solutions.append(board_to_output_format(board))
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens(board, col + 1, solutions)
            board[i][col] = 0


def board_to_output_format(board):
    """Convert the board to the required output format"""
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solution.append([i, j])
    return solution


def print_solutions(solutions):
    """Print all the solutions"""
    for solution in solutions:
        print(solution)


board = [[0 for _ in range(n)] for _ in range(n)]
solutions = []

solve_nqueens(board, 0, solutions)
print_solutions(solutions)
