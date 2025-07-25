# for i in range(4):
#         for i in range(4):
#                 print("x ",end="")
#         print()

# for i in range(1,5,1):
#         for j in range(i):
#            print("x ",end="")
#         print()


width=int(input("What do u wamt ur width to be? (JUST ENTER SEVEN): "))
for i in range(width-1,-1,-1):
    for j in range(i):
        if j!=width:
            print(" ",end="")
    for l in range(i,width,1):
        if l==i or l==width-1:
            print("x ",end="")
        elif i==0 and l==width-4:
            print("BEN",end="")
        else:
            if i==0 and l==width-5:
                print(" ", end="")
            else:
                print("  ",end="")
    print()
for i in range(1,width,1):
    for j in range(i):
        print(" ",end="")
    for l in range(i,width,1):
        if l==i or l==width-1:
            print("x ",end="")
        else:
            print("  ",end="")
    print()


