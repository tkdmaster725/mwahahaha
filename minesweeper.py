import random
board=[]
reallysecretboard=[]
for i in range(10):
    reallysecretboard.append(["_","_","_","_","_","_","_","_","_","_"])
for i in range(10):
    board.append(["_","_","_","_","_","_","_","_","_","_"])
def printy():
    for i in range(10):
        print(board[i])
    print("--------------------------------------------------")
    print("--------------------------------------------------")


def diduwin():
    for i in range(10):
        for j in range(10):
            if board[i][j]=="_" and reallysecretboard[i][j]!="bomb":
                return False
    return True
                
game=True
numberofbombs=random.randint(15,20)
for i in range(numberofbombs):
    bombx=random.randint(0,9)
    bomby=random.randint(0,9)
reallysecretboard[bombx][bomby]="bomb"
while game==True:
    if diduwin()==False:
        printy()
        y=int(input("What column? "))
        x=int(input("What row? "))
        if reallysecretboard[x-1][y-1]=="bomb":
            board[x-1][y-1]="💣"
            printy()
            print("Game over! ")
            game=False
            break
        reallysecretboard[x-1][y-1]="AAAAAAAAAAAAAAAAAAAAAA"
        nearby=0
        if x-2>9 or x-2<0 or y>9 or y<0:
            pass
        else:
            if reallysecretboard[x-2][y]=="bomb":
                nearby+=1
        if x-1>9 or x-1<0 or y>9 or y<0:
            pass
        else:
            if reallysecretboard[x-1][y]=="bomb":
                nearby+=1
        if x>9 or x<0 or y>9 or y<0:
            pass
        else:
            if reallysecretboard[x][y]=="bomb":
                nearby+=1
        if x-2>9 or x-2<0 or y-1>9 or y-1<0:
            pass
        else:
            if reallysecretboard[x-2][y-1]=="bomb":
                nearby+=1
        if x>9 or x<0 or y-1>9 or y-1<0:
            pass
        else:
            if reallysecretboard[x][y-1]=="bomb":
                nearby+=1
        if x-1>9 or x-1<0 or y-2>9 or y-2<0:
            pass
        else:
            if reallysecretboard[x-1][y-2]=="bomb":
                nearby+=1
        if x>9 or x<0 or y-2>9 or y-2<0:
            pass
        else:
            if reallysecretboard[x][y-2]=="bomb":
                nearby+=1
        if x-2>9 or x-2<0 or y-2>9 or y-2<0:
            pass
        else:
            if reallysecretboard[x-2][y-2]=="bomb":
                nearby+=1
        board[x-1][y-1]=str(nearby)
        printy()
    if diduwin()==True:
        print("You win! ")
        game=False
        break