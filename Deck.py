import random
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
        return self.cards.pop()
    def shuffle(self):
        for i in range(len(self.cards)):
            dos=random.randint(0,51)
            uno=self.cards[i]
            self.cards[i]=self.cards[dos]
            self.cards[dos]=uno
    def addcard(self,cardhehe):
        self.cards.append(cardhehe)
        
d=deck()
d.createdeck()
d.shuffle()
d.addcard(card("fours",4))
d.printdeck()