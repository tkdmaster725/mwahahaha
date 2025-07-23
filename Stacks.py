class dfas():
    def __init__(self,data):
        self.data=data
        self.next=None
    def setlink(self,nextthing):
        self.next=nextthing
    def getlink(self):
        return self.next
    def __str__(self):
        return str(self.data)
    
class safd():
    def __init__(self):
        self.size=0
        self.head=None
    def addthing(self,thing):
        if self.size==0:
            self.head=thing
            self.size+=1
        else:
            current=self.head
            for i in range(self.size):
                if current.getlink()==None:
                    current.setlink(thing)
                current.getlink()
                current=current.getlink()
            self.size+=1
    def printthing(self):
        currentt=self.head
        for i in range(self.size):
            print(currentt)
            currentt=currentt.getlink()
    def getout(self,getridof):
        getridof+=1
        currenttt=self.head
        if getridof==1:
            self.head=self.head.getlink()
            self.size-=1
        else:
            for i in range(getridof-2):
                currenttt=currenttt.getlink()
            currenttt.setlink(currenttt.getlink().getlink())
            self.size-=1
    def addinbetween(self,thing,position):
        if self.size == 0:
            self.head = thing
            self.size+=1
        else: 
            if position == 0:
                yeah=self.head
                self.head=thing
                thing.setlink(yeah)
                self.size+=1
            else:    
                currentttt=self.head
                for i in range(position-1):
                    currentttt=currentttt.getlink()
                thing.setlink(currentttt.getlink())
                currentttt.setlink(thing)
                self.size+=1

class stack:
    def __init__(self):
        self.list=safd()
    def add(self,thingy):
        self.list.addinbetween(thingy,0)
    def getridof(self):
        self.list.getout(0)
    def printprint(self):
        self.list.printthing()
s=safd()
ss = stack()
heh=dfas(3)
hehe=dfas(5)
heheh=dfas(7)
ss.add(heh)
ss.add(hehe)
ss.add(heheh)
ss.printprint()
ss.getridof()
ss.printprint()