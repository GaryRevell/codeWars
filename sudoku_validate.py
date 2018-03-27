
"""

Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku
board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also
contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be
invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

"""

def validSolution(board):
    flags = [1 for x in range(0, 9)]
    for row in board:
        rowFlags = flags.copy()
        for col in row:
            if col > 0 and col < 10:
                rowFlags[col - 1] = 0

        if 1 in rowFlags:
            return False

    col = 0
    while col < 9:
        colFlags = flags.copy()
        for row in range(0, 9):
            colFlags[board[row][col] - 1] = 0

        if 1 in colFlags:
            return False
        col += 1

    nines = [[1, 1], [1, 4], [1, 7], [4, 1], [4, 4], [4, 7], [7, 1], [7, 4], [7, 7]]
    for c in nines:
        colFlags = flags.copy()
        for row in range(c[0] - 1, c[0] + 2):
            for col in range(c[1] - 1, c[1] + 2):
                colFlags[board[row][col] - 1] = 0

        if 1 in colFlags:
            return False

    return True

def test_true():
    assert validSolution([
      [5, 3, 4, 6, 7, 8, 9, 1, 2],
      [6, 7, 2, 1, 9, 5, 3, 4, 8],
      [1, 9, 8, 3, 4, 2, 5, 6, 7],
      [8, 5, 9, 7, 6, 1, 4, 2, 3],
      [4, 2, 6, 8, 5, 3, 7, 9, 1],
      [7, 1, 3, 9, 2, 4, 8, 5, 6],
      [9, 6, 1, 5, 3, 7, 2, 8, 4],
      [2, 8, 7, 4, 1, 9, 6, 3, 5],
      [3, 4, 5, 2, 8, 6, 1, 7, 9]]) == True

def test_false():
    assert validSolution([
      [5, 3, 4, 6, 7, 8, 9, 1, 2],
      [6, 7, 2, 1, 9, 0, 3, 4, 8],
      [1, 0, 0, 3, 4, 2, 5, 6, 0],
      [8, 5, 9, 7, 6, 1, 0, 2, 0],
      [4, 2, 6, 8, 5, 3, 7, 9, 1],
      [7, 1, 3, 9, 2, 4, 8, 5, 6],
      [9, 0, 1, 5, 3, 7, 2, 1, 4],
      [2, 8, 7, 4, 1, 9, 6, 3, 5],
      [3, 0, 0, 4, 8, 1, 1, 7, 9]]) == False

    assert validSolution([
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]]) == False

if __name__ == "__main__":
    test_true()
    test_false()

