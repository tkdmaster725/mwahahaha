board=[["_","_","_","_","_","_","_","_"],
       ["_","_","_","_","_","_","_","_"],
       ["_","_","_","_","_","_","_","_"],
       ["_","_","_","_","_","_","_","_"],
       ["_","_","_","_","_","_","_","_"],
       ["_","_","_","_","_","_","_","_"],
       ["_","_","_","_","_","_","_","_"],
       ["_","_","_","_","_","_","_","_"]]

class pawn:
    def __init__(self,color,row,col):
        self.color=color
        self.row = row
        self.col = col
    def legalmoves(self):
        if self.color=="w":
            return [(self.row-1,self.col),(self.row-2,self.col)]
        if self.color=="b":
            return [(self.row+1,self.col),(self.row+2,self.col)]
    def cantake(self):
        if self.color=="b":
            [(self.row+1,self.col+1),(self.row+1,self.col-1)]
        if self.color=="w":
            [(self.row+1,self.col+1),(self.row+1,self.col-1)]
    
myboard = [pawn("w", 1,1), pawn("w")]