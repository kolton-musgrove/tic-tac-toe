import random


def main():
    print("Welcome to TicTacToe")
    # (The player is always x, the computer always O. player always starts.)
    board = createBoard()

    # Create game board
    gameLoop(board)


def gameLoop(board):
    # play loop:
    while True:
        # display game board
        printBoard(board)
        # move make
        while True:
            print("Where would you like to move? ")
            move = int(input("Move (1-9): "))

            if validMove(board, move):
                break
            else:
                print("please enter a valid move")

        # make move
        board = makeMove(board, move, "X")

        # win condition check
        if winCondition(board):
            printBoard(board)
            print("You won!")
            exit()

        computerMove(board)

        if winCondition(board):
            printBoard(board)
            print("The computer won!!!")
            exit()


def createBoard():
    return [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def printBoard(board):
    print("", board[0], "|", board[1], "|", board[2], "")
    print("----------")
    print("", board[3], "|", board[4], "|", board[5], "")
    print("----------")
    print("", board[6], "|", board[7], "|", board[8], "")


def winCondition(board):
    # horizontal
    if (
        board[0] == board[1]
        and board[1] == board[2]
        and " " not in [board[0], board[1], board[2]]
    ):
        return True
    if (
        board[3] == board[4]
        and board[4] == board[5]
        and " " not in [board[3], board[4], board[5]]
    ):
        return True
    if (
        board[6] == board[7]
        and board[7] == board[8]
        and " " not in [board[6], board[7], board[8]]
    ):
        return True

    # vertical
    if (
        board[0] == board[3]
        and board[3] == board[6]
        and " " not in [board[0], board[3], board[6]]
    ):
        return True
    if (
        board[1] == board[4]
        and board[4] == board[7]
        and " " not in [board[1], board[4], board[7]]
    ):
        return True
    if (
        board[2] == board[5]
        and board[5] == board[8]
        and " " not in [board[2], board[5], board[8]]
    ):
        return True

    # diagonal
    if (
        board[0] == board[4]
        and board[4] == board[8]
        and " " not in [board[0], board[4], board[8]]
    ):
        return True
    if (
        board[2] == board[4]
        and board[4] == board[6]
        and " " not in [board[2], board[4], board[6]]
    ):
        return True

    return False


def validMove(board, move):
    # use array indexing
    move = move - 1

    checkForCatsGame(board)

    # check if the move is withing the correct domain
    if move < 0 or move > 8:
        print("please supply a number between 1 and 9.")
        return False
    # select if the move is in a currently blank space
    elif board[move] != " ":
        print("please select a move in a blank space")
        return False
    return True


def makeMove(board, move, player):
    # use array indexing
    move = move - 1
    board[move] = player
    return board


def computerMove(board):
    moveMade = False
    while moveMade == False:
        potentialMove = random.randrange(0, 8)
        if validMove(board, potentialMove):
            makeMove(board, potentialMove, "O")
            moveMade = True


def checkForCatsGame(board):
    if " " not in [
        board[0],
        board[1],
        board[2],
        board[3],
        board[4],
        board[5],
        board[6],
        board[7],
        board[8],
    ]:
        print("Guess it's a cat's game. What a shame.")
        exit()


main()
