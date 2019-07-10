import os
board = [[], [], [], [], [], [], []]
player =2
turn=0
win = False
def display():
    os.system("clear")
    print("╔═══╦═══╦═══╦═══╦═══╦═══╦═══╗")
    for c in range (5, -1, -1):
        print("║", end ="")
        for r in range (7):
            try:
                if board[r][c] == 1:
                    piece = "O"
                else:
                    piece = "X"
                print("", piece, "║", end = "")
            except IndexError as e:
                print("  ", "║", end = "")     
        print("")
        if c > 0 :
            print("╠═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
        else:
            print("╚═══╩═══╩═══╩═══╩═══╩═══╩═══╝")
    print("  1   2   3   4   5   6   7")    

def play(col):
    board[col-1].append(player)
    display()
  

def winning_move(board,col,win,colheight):
    #condition colonne
    if colheight >= 4 :
        if board[col-1][colheight-1] == board[col-1][colheight-2] == board[col-1][colheight-3] == board[col-1][colheight-4]:
            return win 
        else:
            return win
    #condition ligne
    





display()
win = False
while win == False:    
    if player == 1:
        player = 2
    else:
        player = 1
    print("It's Player",player,"'s Turn")
    col = int(input("Which column do you want to play ?"))
    play(col)
    colheight= len(board[col-1])
    winning_move(board,col,win,colheight)
    turn= turn+1
if win== True :
    print("gg, player",player,"You win !")
    
