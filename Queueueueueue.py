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
        if self.size==0:
            self.head=thing
        else:
            currentttt=self.head
            for i in range(position-1):
                currentttt=currentttt.getlink()
            thing.setlink(currentttt.getlink())
            currentttt.setlink(thing)
        self.size+=1
class queue:
    def __init__(self):
        self.yeah=safd()
    def remove(self):
        self.yeah.getout(1)
    def addadd(self,thing):
        self.yeah.addinbetween(thing,0)
hi=queue()
ha=dfas(3)
he=dfas(2)
hahe=dfas(1)
hi.addadd(ha)
hi.addadd(he)
hi.addadd(hahe)
hi.remove()
hi.yeah.printthing()