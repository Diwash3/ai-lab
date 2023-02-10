#Tic-Tac-Toe
import os 

turn='x'
win=False
space=9
def draw(board):
    for i in range(6,-1,-3):
        print(""+board[i]+'|'+board[i+1]+'|'+board[i+2])

def takeinput(board,space,turn):
    pos=-1
    print(turn+"s turn")
    while pos==-1:
        try:
            print("pick position 0-9")
            pos=int(input())
            if (pos<0 or pos>9):
                pos=-1
            elif board[pos-1]!='':
                pos=-1
        except:
            print("pick a correct position")
    space-=1 
    board[pos-1]=turn
    if turn=='x':
        turn=='o';
    else:
        turn='x'
    return board,space,turn

def checkin(board):
    for i in range(0,3):
        r=i*3 
        if board[r]!='':
            if board[r]==board[r+1] and board[r+1]==board[r+2]:
                return board[r]
        if board[i]!='':
            if board[i]==board[i+3] and board[i]==board[i+6]:
                return board[i]
        if board[0]!='':
            if board[0]==board[4] and board[4]==board[8]:
                return board[0]
        if board[2]!='':
            if board[2]==board[4] and board[4]==board[6]:
                return board[2]
    return 0 
board=['']*9 
while not win and space:
    draw(board)
    board,space,turn=takeinput(board,space,turn)
    win=checkin(board)
    os.system('cls')
    
draw(board)
if not win and space:
    print("draw")
else:
    print(f"{win}wins")
    input()

