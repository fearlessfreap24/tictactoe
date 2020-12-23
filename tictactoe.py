import random
import re


def isWin(player):
    wins = [{0,1,2}, {3,4,5}, {6,7,8}, {0,3,6}, {1,4,7}, {2,5,8}, {0,4,8}, {2,4,6}]
    if len(player['moves']) < 3:
        return False
    for win in wins:
        if win.issubset(player["moves"]):
            return True
    return False


def printBoard(user, computer, initial=False):
    board = list()
    for i in range(9):
        if i in user["moves"]:
            board.append(user["token"])
        elif i in computer["moves"]:
            board.append(computer["token"])
        else:
            if initial:
                board.append(str(i + 1))
            else:
                board.append(" ")
    
    print(f"\n{board[0]} | {board[1]} | {board[2]}\n_________\n{board[3]} | {board[4]} | {board[5]}\n_________\n{board[6]} | {board[7]} | {board[8]}\n")


def getUserToken():
    userTokenInput = input("Select your token, [X] or [O] : ").upper()
    while userTokenInput != "X" and userTokenInput != "O":
        print(f"Your selection of \"{userTokenInput}\" is invalid. Please select [X] or [O] : ")
        userTokenInput = input("Select your token, [X] or [O] : ").upper()
    return userTokenInput


def whoGoesFirst():
    userFirst = random.randint(0,99) % 2 == 0
    if userFirst:
        print("\nYou have been selected to go first")
        return True
    else:
        print("\nThe Computer has been selected to go first")
        return False


def getUserMove():
    numbers = r'[123456789]'
    userInput = input("Please select an available space to play: (numbers only) ")
    while not re.findall(numbers, userInput) or len(userInput) > 1:
        userInput = input("Please select a valid number between 1 and 9: (numbers only) ")
    return int(userInput) - 1



def tictactoe():
    user = {"token": getUserToken(), "moves": set()}
    comp = {"token": "X" if user["token"] == "O" else "O", "moves": set()}
    
    print(f"You are \"{user['token']}'s\" and the Computer is \"{comp['token']}'s\"")

    availableMoves = set( i for i in range(9))
    isUserTurn = whoGoesFirst()
    userWin = False
    compWin = False

    printBoard(user, comp, initial=True)

    while len(availableMoves) > 0 and not userWin and not compWin:
        if isUserTurn:
            userMove = getUserMove()
            while userMove not in availableMoves:
                userMove = getUserMove()
            user["moves"].add(userMove)
            availableMoves.remove(userMove)
            isUserTurn = False
            userWin = isWin(user)
        else:
            compMove = random.randint(0, 8)
            while compMove not in availableMoves:
                compMove = random.randint(0, 8)
            comp["moves"].add(compMove)
            availableMoves.remove(compMove)
            isUserTurn = True
            compWin = isWin(comp)
        
        printBoard(user, comp)

    if userWin:
        print(f"\nCongratulations!!! you, the \"{user['token']}'s\" have won!\n")
    elif compWin:
        print(f"\nUnfortunatley you have lost. The Computer,  \"{comp['token']}'s\", have won!\n")
    else:
        print("\nThe game is a draw\n")
    
    printBoard(user, comp)


if __name__ == "__main__":
    tictactoe()
