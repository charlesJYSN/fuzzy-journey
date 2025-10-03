for i in range(1,11,1):
    for o in range(10,i,-1):
        print(" ",end="")
    for y in range(i,0,-1):
        print(y,end="")
    for x in range(2,i + 1, 1):
        print(x,end="")
    print()
