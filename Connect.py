import os
board = [[], [], [], [], [], [], []]
player =1
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

def play():
    col = int(input("Which column do you want to play ?"))    
    #Si cette ligne n'est pas là le joueur ne peut pas jouer la colonne 7 
    board[col-1].append(player)
    display()
  

def winning_move(board,col):
    win = False







display()
while True:    
    print("It's Player",player,"'s Turn")
    play()
    print(col)
    print(boardheight)
    if player == 1:
        player = 2
    else:
        player = 1