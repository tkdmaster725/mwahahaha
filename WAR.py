import random
import time
class card:
    def __init__(self,suit,value):
        self.suit=suit
        self.value=value
    def __str__(self):
        return str(self.value) + " of " + self.suit
class deck:
    def __init__(self):
        self.cards=[]
    def createdeck(self):
        x=1
        for i in range(13):
          self.cards.append(card("hearts",x))
          self.cards.append(card("clubs",x))
          self.cards.append(card("diamonds",x))
          self.cards.append(card("spades",x))
          x=x+1
    def printdeck(self):
        for i in range(len(self.cards)):
           print(self.cards[i])
    def drawcard(self):
        return self.cards.pop(0)
    def shuffle(self):
        for j in range(100):
            for i in range(len(self.cards)):
                dos=random.randint(0,len(self.cards)-1)
                uno=self.cards[i]
                self.cards[i]=self.cards[dos]
                self.cards[dos]=uno
    def addcard(self,cardhehe):
        self.cards.append(cardhehe)
    def decklengthy(self):
        return len(self.cards)



d=deck()
d.createdeck()
d.shuffle()
player1=deck()
player2=deck()
tiedeckthingie=deck()
for i in range(26):
    player1.addcard(d.drawcard())
    player2.addcard(d.drawcard())
game=True
while player1.decklengthy()>0 and player2.decklengthy()>0 and game==True:
    yeah=player1.drawcard()
    yup=player2.drawcard()
    print("Player 1's card: "+ str(yeah))
    print("Player 2's card: "+ str(yup))
    while yup.value==yeah.value:
        if player1.decklengthy()<4:
            print("Player 1 didn't have enough cards for war and lost! ")
            game=False
            break
        elif player2.decklengthy()<4:
            print("Player 2 didn't have enough cards for war and lost! ")
            game=False
            break
        else:
            print("It's a tie! WAR! ")
            tiedeckthingie.addcard(yeah)
            tiedeckthingie.addcard(player1.drawcard())
            tiedeckthingie.addcard(player1.drawcard())
            tiedeckthingie.addcard(player1.drawcard())
            yeah4=player1.drawcard()
            tiedeckthingie.addcard(yeah4)
            tiedeckthingie.addcard(yup)
            tiedeckthingie.addcard(player2.drawcard())
            tiedeckthingie.addcard(player2.drawcard())
            tiedeckthingie.addcard(player2.drawcard())
            yup4=player2.drawcard()
            tiedeckthingie.addcard(yup4)
            tiedeckthingie.shuffle()
            print("Player 1's card: "+ str(yeah4))
            print("Player 2's card: "+ str(yup4))
            if yup4.value>yeah4.value:
                print("Player 2 won the WAR! Going again... ")
                time.sleep(1)
                for i in range(tiedeckthingie.decklengthy()):
                    player2.addcard(tiedeckthingie.drawcard())
                break

            elif yup4.value<yeah4.value:
                print("Player 1 won the WAR! Going again... ")
                time.sleep(1)
                for i in range(tiedeckthingie.decklengthy()):
                    player1.addcard(tiedeckthingie.drawcard())
                break


    if yup.value>yeah.value:
        print("Player 2 won! Going again... ")
        player2.addcard(yeah)
        player2.addcard(yup)
        print(player1.decklengthy())
        print(player2.decklengthy())
    elif yup.value<yeah.value:
        print("Player 1 won! Going again... ")
        player1.addcard(yeah)
        player1.addcard(yup)
        print(player1.decklengthy())
        print(player2.decklengthy())