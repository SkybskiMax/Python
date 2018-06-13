import itertools
board = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
         [6, 7, 2, 1, 9, 5, 3, 4, 8],
         [1, 9, 8, 3, 4, 2, 5, 6, 7],
         [8, 5, 9, 7, 6, 1, 4, 2, 3],
         [4, 2, 6, 8, 5, 3, 7, 9, 1],
         [7, 1, 3, 9, 2, 4, 8, 5, 6],
         [9, 6, 1, 5, 3, 7, 2, 8, 4],
         [2, 8, 7, 4, 1, 9, 6, 3, 5],
         [3, 4, 5, 2, 8, 6, 1, 7, 9]]


def validSolution(board):
    return checkRows(board) and checkColumns(board) and checkBoxes(board)

def checkRows(board):
    for row in board:
        if (ifProperArray(row)):
            pass
        else: return False
    return True

def checkColumns(board):
    for j in range(0,9):
        column = []
        for i in range(0,9):
            column.append(board[i][j])
        if (ifProperArray(column)):
            pass
        else: return False
    return True

def checkBoxes(board):
    for i in range(0,9,3):
        for j in range(0,9,3):
            square = list(itertools.chain(row[j:j + 3] for row in board[i:i + 3]))
            squareVect = []
            for k in square:
                for number in k:
                   squareVect.append(number)
            if (ifProperArray(squareVect)):
                pass
            else:
                return False
    return True


def ifProperArray(array):
    if sorted(array) == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return True
    else:
        return False


print(validSolution(board))




