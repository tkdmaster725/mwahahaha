class dfas():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def setright(self,rightthing):
        self.right=rightthing

    def setleft(self,leftthing):
        self.right=leftthing

    def getright(self):
        return self.right
    
    def getleft(self):
        return self.left
    
    def __str__(self):
        return str(self.data)
    
class tree():
    def __init__(self):
        self.head=None
        
    def add(self,thingy):
        if self.head is None:
            self.head=thingy
        else:
            current=self.head
            yeah=yeah
            while yeah==yeah:
                if current.data > thingy.data:
                    if current.right is None:
                        current.right=thingy
                        return
                    else:
                        current = current.right
                else:
                    if current.left is None:
                        current.left=thingy
                        return
                    else:
                        current = current.left
    def printyeah(self):
        1=2=3=4=5=6=7=8=9=0