"""
Exercise: Tic-Tac-Toe Board

Description:
Demonstrates a simple board layout and turn-based input flow.
"""


theBoard = {
    "top-L": " ",
    "top-M": " ",
    "top-R": " ",
    "mid-L": " ",
    "mid-M": " ",
    "mid-R": " ",
    "low-L": " ",
    "low-M": " ",
    "low-R": " ",
}


def printBoard(board):
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])


printBoard(theBoard)

turn = "X"
for i in range(9):
    printBoard(theBoard)
    print("Turn for " + turn + ". Move on which space?")
    move = input()
    theBoard[move] = turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"


def check_winner(board):
    (1, 2, 3) (4, 5, 6) (7, 8, 9)  # possible winning conditions 1
    (1, 4, 7) (2, 5, 8) (3, 6, 9)  # 2
    (1, 5, 9) (3, 5, 7)  # 3


print(check_winner)


