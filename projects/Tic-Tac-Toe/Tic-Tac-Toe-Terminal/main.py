# create a tic-tac-toe game

import random


def drawBoard(board):
    # This function prints out the board that it was passed.
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print(f" {board[7]} | {board[8]} | {board[9]}")
    print("-----------")
    print(f" {board[4]} | {board[5]} | {board[6]}")
    print("-----------")
    print(f" {board[1]} | {board[2]} | {board[3]}")


def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player’s letter as the first item, and the computer's letter as the second.
    letter = ""
    while letter not in {"X", "O"}:
        print("Do you want to be X or O?")
        letter = input().upper()

    # the first element in the list is the player’s letter, the second is the computer's letter.
    return ["X", "O"] if letter == "X" else ["O", "X"]


def whoGoesFirst():
    # Randomly choose the player who goes first.
    return "computer" if random.randint(0, 1) == 0 else "player"


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don’t have to type as much.
    return (
        (bo[7] == le and bo[8] == le and bo[9] == le)
        or (bo[4] == le and bo[5] == le and bo[6] == le)  # across the top
        or (bo[1] == le and bo[2] == le and bo[3] == le)  # across the middle
        or (bo[7] == le and bo[4] == le and bo[1] == le)  # across the bottom
        or (bo[8] == le and bo[5] == le and bo[2] == le)  # down the left side
        or (bo[9] == le and bo[6] == le and bo[3] == le)  # down the middle
        or (bo[7] == le and bo[5] == le and bo[3] == le)  # down the right side
        or (bo[9] == le and bo[5] == le and bo[1] == le)  # diagonal
    )  # diagonal


def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    return board[:]  # slicing the list to include all items


def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == " "


def getPlayerMove(board):
    # Let the player type in their move.
    move = " "
    while move not in "1 2 3 4 5 6 7 8 9".split() or not isSpaceFree(board, int(move)):
        print("What is your next move? (1-9)")
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, movesList):
    possibleMoves = [i for i in movesList if isSpaceFree(board, i)]
    return random.choice(possibleMoves) if possibleMoves else None


def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    playerLetter = "O" if computerLetter == "X" else "X"
    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move is None:
            # Try to take the center, if it is free.
        return (
            5
            if isSpaceFree(board, 5)
            else chooseRandomMoveFromList(board, [2, 4, 6, 8])
        )
    else:
        return move


def isBoardFull(board):
    return not any(isSpaceFree(board, i) for i in range(1, 10))


print("Welcome to Tic Tac Toe!")

while True:
    # Reset the board
    theBoard = [" "] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print(f"The {turn} will go first.")
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == "player":
            # Player’s turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("Hooray! You have won the game!")
                gameIsPlaying = False
            elif isBoardFull(theBoard):
                drawBoard(theBoard)
                print("The game is a tie!")
                break
            else:
                turn = "computer"

        else:
            # Computer’s turn.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("The computer has beaten you! You lose.")
                gameIsPlaying = False
            elif isBoardFull(theBoard):
                drawBoard(theBoard)
                print("The game is a tie!")
                break
            else:
                turn = "player"

    if not playAgain():
        break
