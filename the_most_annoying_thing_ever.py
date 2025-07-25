
def solve_hanoi(peg, current, helper, goal):
    if peg>0:
        solve_hanoi(peg-1, current, goal, helper)
        print("Move disk "+ str(peg) + " from peg " + str(current) + " to peg " + str(goal))
        solve_hanoi(peg-1, helper, current, goal) 
solve_hanoi(50,1,2,3)
exit()   




peguno=[9,8,7,6,5,4,3,2,1]
pegdos=[]
pegtres=[]
total = len(peguno)
def printt():
    print(peguno)
    print(pegdos)
    print(pegtres)
    print("--")
printt()
def moveone():
    if 1 in peguno:
        pegtres.append(1)
        peguno.remove(1)
        return 3
    if 1 in pegdos:
        peguno.append(1)
        pegdos.remove(1)
        return 1
    if 1 in pegtres:
        pegdos.append(1)
        pegtres.remove(1)
        return 2
def move(thing1,thing2):
    if len(thing1)==0:
        thing1.append(thing2.pop(len(thing2)-1))
    elif len(thing2)==0:
        thing2.append(thing1.pop(len(thing1)-1))
    elif thing1[len(thing1)-1] > thing2[len(thing2)-1]:
        thing1.append(thing2.pop(len(thing2)-1))
    else:
        thing2.append(thing1.pop(len(thing1)-1))
while len(pegtres)!=total:
    x = moveone()
    if len(pegtres)==total:
        printt()
        exit()
    printt()
    if x == 1:
        move(pegdos,pegtres)
    elif x == 2:
        move(pegtres,peguno)
    else:
        move(peguno,pegdos)
    printt()