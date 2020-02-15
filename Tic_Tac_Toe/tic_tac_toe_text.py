board = [' ' for x in range(10)]


def insert_board(letter, pos):
    board[pos] = letter


def space_is_free(pos):
    return board[pos] == ' '


def is_winner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))


def player_move():
    run = True
    while run:
        move = input("Enter positions (1-9) to place an \'X\': ")
        try:
            move = int(move)
            if 0 < move < 10:
                if space_is_free(move):
                    run = False
                    insert_board('X', move)
                else:
                    print("Invalid input")
            else:
                print("Enter a number within the range")
        except TypeError:
            print("Type a number")


def select_random(li):
    import random
    n = len(li)
    r_int = random.randrange(0, n)
    return li[r_int]


def comp_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0

    for let in ["O", "X"]:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move

    open_corners = [i for i in possible_moves if i in [1, 3, 7, 9]]

    if len(open_corners) > 0:
        move = select_random(open_corners)
        return move

    if 5 in possible_moves:
        move = 5
        return move

    open_edges = [i for i in possible_moves if i in [2, 4, 6, 8]]

    if len(open_edges) > 0:
        move = select_random(open_edges)

    return move


def is_board_full(bo):
    return not bo.count(" ") > 1


def print_board():
    print('   |   |')
    print(" " + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-------------')
    print('   |   |')
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print('   |   |')
    print('-------------')
    print('   |   |')
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print('   |   |')


def main():
    print_board()

    while not(is_board_full(board)):
        if not is_winner(board, "O"):
            player_move()
            print_board()
        else:
            print("O wins")
            break

        if not is_winner(board, "X"):
            move = comp_move()
            if move == 0:
                print("Game tie!")
            else:
                insert_board('O', move)
                print("Computer placed \'O\' in position", move)
                print_board()
        else:
            print("X wins")
            break
    if is_board_full(board):
        print("Tie game!")


while True:
    answer = input("Do you want to play?")
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print("-------------------------------------")
        main()
    else:
        break
