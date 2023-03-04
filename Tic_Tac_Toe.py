def sum(a,b,c):
    return a+b+c
def board(x,y):
    zero='X' if x[0] else ('Y' if y[0] else 0)
    one='X' if x[1] else ('Y' if y[1] else 0)
    two='X' if x[2] else ('Y' if y[2] else 0)
    three='X' if x[3] else ('Y' if y[3] else 0)
    four='X' if x[4] else ('Y' if y[4] else 0)
    five='X' if x[5] else ('Y' if y[5] else 0)
    six='X' if x[6] else ('Y' if y[6] else 0)
    seven='X' if x[7] else ('Y' if y[7] else 0)
    eight='X' if x[8] else ('Y' if y[8] else 0)
    
    print(f"{zero}|{one}|{two}")
    print("-|-|-")
    print(f"{three}|{four}|{five}")
    print("-|-|-")
    print(f"{six}|{seven}|{eight}")
def check_win(x,y):
    winner=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in winner:
        if (sum(x[win[0]],x[win[1]],x[win[2]])==3):
            print("x wom the match")
            return 1
        if (sum(y[win[0]],y[win[1]],y[win[2]])==3):
            print("Y won the match")
            return 0
    return -1
        
x=[0,0,0,0,0,0,0,0,0]
y=[0,0,0,0,0,0,0,0,0]
turn=1
print("welcome!!")
while True:
    board(x,y)
    if turn==1:
        print("x's chance")
        value=int(input("please Enter a value:"))
        x[value]=1
    else: 
        print("Y's chance:")
        value=int(input("please enter a value:"))
        y[value]=1
    cwin=check_win(x,y)
    if cwin!=-1:
        break
    turn=1-turn
