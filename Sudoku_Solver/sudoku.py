import numpy as np

board = [[3, 0, 1],
        [0, 0, 2],
        [1, 2, 0]]


def print_board(bo):
    for i in range(len(bo)):
        if i % 1 == 0 and i != 0:
            print("-------------")

        for j in range(len(bo[0])):
            if j % 1 == 0 and j != 0:
                print(" | ", end="")

            if j == 2:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j

    return None

