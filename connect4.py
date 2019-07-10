import os


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
  

def winning_move(board, last_col):
    return False

    # #condition colonne
    # if colheight >= 4 :
    #     if board[col-1][colheight-1] == board[col-1][colheight-2] == board[col-1][colheight-3] == board[col-1][colheight-4]:
    #         win = True
    #         return win
    # #condition ligne
    # try:
    #     if board[col-1][colheight-1] == board[col][colheight-1] == board[col+1][colheight-1] == board[col+2][colheight-1]:
    #         win = True
    #         return win
    # except:
    #     pass
    # try:
    #     if board[col-2][colheight-1] == board[col-1][colheight-1] == board[col][colheight-1] == board[col+1][colheight-1]:
    #         win = True
    #         return win
    # except:
    #     pass
    # try:
    #     if board[col-3][colheight-1] == board[col-2][colheight-1] == board[col-1][colheight-1] == board[col][colheight-1]:
    #         win = True
    #         return win
    # except:
    #     pass
    # try:
    #     if board[col-4][colheight-1] ==board[col-3][colheight-1] == board[col-2][colheight-1] ==  board[col-1][colheight-1]:
    #         win = True
    #         return win
    # except:
    #     pass
    #diagonales croissantes
    # try:
    #     if board[col-1][colheight-1] == board[col][colheight] == board[col+1]
    # except:
    #     pass

def run():
    board = [[], [], [], [], [], [], []]
    player =2
    turn=0
    win = False    
    display()
    while win != True:    
        if player == 1:
            player = 2
        else:
            player = 1
        print("It's Player",player,"'s Turn")
        col = int(input("Which column do you want to play ?"))
        play(col)
        colheight= len(board[col-1])
        winning_move(board,col,win,colheight)
        win = winning_move(board,col,win,colheight)
        turn= turn+1
    if win== True :
        print("gg, player",player,"You win !")
    
    
if __name__ == "__main__":
    run()