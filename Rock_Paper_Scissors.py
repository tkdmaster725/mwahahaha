import random

compwins=0
playerwins=0
games=0

while games>=0 and games<=2:
    playerchoice=input("What do u want to pick? ")
    computerchoice=random.randint(1,3)

    if computerchoice==1:
        if playerchoice=="Rock":
            print("The computer picked rock. Tie!")
            print("The score is " + str(playerwins) + " to " + str(compwins))
        if playerchoice=="Paper":
            print("The computer picked rock. You won!")
            games=games+1
            playerwins=playerwins+1
            print("The score is " + str(playerwins) + " to " + str(compwins))
        if playerchoice=="Scissors":
            print("The computer picked rock. You lost! oof")
            games=games+1
            compwins=compwins+1
            print("The score is " + str(playerwins) + " to " + str(compwins))
    elif computerchoice==2:
        if playerchoice=="Rock":
            print("The computer picked paper. You lost! sad")
            games=games+1
            compwins=compwins+1
            print("The score is " + str(playerwins) + " to " + str(compwins))
        if playerchoice=="Paper":
            print("The computer picked paper. Tie!")
            print("The score is " + str(playerwins) + " to " + str(compwins))
        if playerchoice=="Scissors":
            print("The computer picked paper. You won!")
            games=games+1
            playerwins=playerwins+1
            print("The score is " + str(playerwins) + " to " + str(compwins))
    elif computerchoice==3:
        if playerchoice=="Rock":
            print("The computer picked scissors. You won!")
            playerwins=playerwins+1
            games=games+1
            print("The score is " + str(playerwins) + " to " + str(compwins))
        if playerchoice=="Paper":
            print("The computer picked scissors. You lost! aww")
            games=games+1
            compwins=compwins+1
            print("The score is " + str(playerwins) + " to " + str(compwins))
        if playerchoice=="Scissors":
            print("The computer picked scissors. Tie!")
            print("The score is " + str(playerwins) + " to " + str(compwins))

if playerwins==2 and compwins==1:
    print("You Won!! Yay!")
elif playerwins==3 and compwins==0:
    print("You Won!! Yay!")
elif playerwins==1 and compwins==2:
    print("You lost! To a computer.")
elif playerwins==0 and compwins==3:
    print("Yeah, you lost pretty badly...")
    