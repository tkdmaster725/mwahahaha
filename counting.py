def count_up(x,y):
    if x<=y:
        print(x)
        count_up(x+1,y)

def count_down(x):
    if x>=0:
        print(x)
        count_down(x-1)

count_down(5)
