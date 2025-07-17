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
    def computerdecks(self):
        for i in range(99):
            self.cards.append(card("computers",7))
        for i in range(1):
            self.cards.append(card("computers",6))
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
def valueaddedup(list):
    x=0
    for i in range(len(list)):
        x=x+list[i].value
    return x
def convert(cards):
    if cards.value>10:
        cards.value=10
    return cards

d=deck()
d.createdeck()
d.shuffle()
computerdeck=deck()
computerdeck.computerdecks()
computerdeck.shuffle()
hi=[]
totalmoney=2500
game=True
while game==True:
    bet=int(input("How much do you want to bet? You have $" + str(totalmoney) + " "))
    if bet<1 or bet>totalmoney:
        print("Invalid bet! Try again! ")
    else:
        onecard=convert(d.drawcard())
        twocard=convert(d.drawcard())
        hi.append(onecard)
        hi.append(twocard)
        comp1=convert(computerdeck.drawcard())
        comp2=convert(computerdeck.drawcard())
        comp3=convert(computerdeck.drawcard())
        print("The computer's first card is "+str(comp1)+".")
        hitorstand=input("Your first cards are a " + str(onecard) + " and a " + str(twocard) +". Do you want to hit or stand? ")
        if hitorstand=="stand":
            print("",end="")
        while hitorstand=="hit":
            yeah=convert(d.drawcard())
            hi.append(yeah)
            print("You got a "+str(yeah.value)+".")
            print("Your hand: "+ str(valueaddedup(hi)))
            if valueaddedup(hi)>21:
                play2=input("Bust! Do you want to go again? ")
                if play2=="no":
                    game=False
                    break
                if play2=="yes":
                    hi=[]
                    totalmoney=totalmoney-bet
            else:
                hitorstand=input("Your cards add up to "+str(valueaddedup(hi))+". Do you want to hit or stand? ")
    comp1=computerdeck.drawcard()
    comp2=computerdeck.drawcard()
    comp3=computerdeck.drawcard()
    compsum=comp1.value + comp2.value + comp3.value
    if valueaddedup(hi)<compsum:
        print("The computer's cards were "+str(comp1.value)+", "+str(comp2.value)+", and "+str(comp3.value)+".")
        play1=input("You lost! Do you want to go again? ")
        if play1=="no":
            game=False
            break
        if play1=="yes":
            hi=[]
            totalmoney=totalmoney-bet
    elif valueaddedup(hi)>compsum and valueaddedup(hi)<=21:
        print("The computer's cards were "+str(comp1.value)+", "+str(comp2.value)+", and "+str(comp3.value)+".")
        play1=input("You somehow won! Do you want to go again? ")
        if play1=="no":
            game=False
            break
        if play1=="yes":
            totalmoney=totalmoney+bet
            
    elif valueaddedup(hi)==compsum:
        print("The computer's cards were "+str(comp1.value)+", "+str(comp2.value)+", and "+str(comp3.value)+".")
        play1=input("Push! Do you want to go again? ")
        if play1=="no":
            game=False
            break
        if play1=="yes":
            hi=[]
    if valueaddedup(hi)>21:
        play2=input("Bust! Do you want to go again? ")
        if play2=="no":
            game=False
            break
        if play2=="yes":
            hi=[]
            totalmoney=totalmoney-bet
    if totalmoney<=0:
        print("You lost all of your money! ")
        game=0
        break