import time
import random
board=[["_", "_", "_"],["_", "_", "_"],["_", "_", "_"]]
game=0
turns=0

print(board[0])
print(board[1])
print(board[2])
while game==0:
    playerrow=int(input("Which row do you want? "))
    playercolumn=int(input("Which column do you want? "))
    while board[playerrow-1][playercolumn-1]=="x" or board[playerrow-1][playercolumn-1]=="o":
        if board[playerrow-1][playercolumn-1]=="x" or board[playerrow-1][playercolumn-1]=="o":
            print("Try again!")
            playerrow=int(input("Which row do you want? "))
            playercolumn=int(input("Which column do you want? "))
    board[playerrow-1][playercolumn-1]="x"

    print(board[0])
    print(board[1])
    print(board[2])
    print()
    turns=turns+1

    if board[0][0] == "x" and board[0][1] == "x" and board[0][2]=="x":
        print("You won!")
        game=1
        break
    elif board[1][0] == "x" and board[1][1] == "x" and board[1][2]=="x":
        print("You won!")
        game=1
        break
    elif board[2][0] == "x" and board[2][1] == "x" and board[2][2]=="x":
        print("You won!")
        game=1
        break
    elif board[0][0] == "x" and board[1][0] == "x" and board[2][0]=="x":
        print("You won!")
        game=1
        break
    elif board[0][1] == "x" and board[1][1] == "x" and board[2][1]=="x":
        print("You won!")
        game=1
        break
    elif board[0][2] == "x" and board[1][2] == "x" and board[2][2]=="x":
        print("You won!")
        game=1
        break
    elif board[0][0] == "x" and board[1][1] == "x" and board[2][2]=="x":
        print("You won!")
        game=1
        break
    elif board[0][2] == "x" and board[1][1] == "x" and board[2][0]=="x":
        print("You won!")
        game=1
        break
    elif turns==9:
        print("Tie!")
        game=1
        break
    

    print("The computer is thinking...")
    print()
    time.sleep(1)
    
    comprow=random.randint(1,3)
    compcolumn=random.randint(1,3)

    while board[comprow-1][compcolumn-1]=="x" or board[comprow-1][compcolumn-1]=="o":
        if board[comprow-1][compcolumn-1]=="x" or board[comprow-1][compcolumn-1]=="o":
            comprow=random.randint(1,3)
            compcolumn=random.randint(1,3)
    board[comprow-1][compcolumn-1]="o"

    print(board[0])
    print(board[1])
    print(board[2])
    print()
    turns=turns+1

    if board[0][0] == "o" and board[0][1] == "o" and board[0][2]=="o":
        print("You lost!")
        game=1
        break
    elif board[1][0] == "o" and board[1][1] == "o" and board[1][2]=="o":
        print("You lost!")
        game=1
        break
    elif board[2][0] == "o" and board[2][1] == "o" and board[2][2]=="o":
        print("You lost!")
        game=1
        break
    elif board[0][0] == "o" and board[1][0] == "o" and board[2][0]=="o":
        print("You lost!")
        game=1
        break
    elif board[0][1] == "o" and board[1][1] == "o" and board[2][1]=="o":
        print("You lost!")
        game=1
        break
    elif board[0][2] == "o" and board[1][2] == "o" and board[2][2]=="o":
        print("You lost!")
        game=1
        break
    elif board[0][0] == "o" and board[1][1] == "o" and board[2][2]=="o":
        print("You lost!")
        game=1
        break
    elif board[0][2] == "o" and board[1][1] == "o" and board[2][1]=="o":
        print("You lost!")
        game=1
        break
    elif turns==9:
        print("Tie!")
        game=1
        break
    