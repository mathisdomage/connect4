import os
from robotlvl2 import robot_testvalue

WINNING_RULES = (
    # vertical
    (( 0, -3), ( 0, -2), ( 0, -1)),

    # horizontal
    ((-3,  0), (-2,  0), (-1,  0)),
    ((-2,  0), (-1,  0), ( 1,  0)),
    ((-1,  0), ( 1,  0), ( 2,  0)),
    (( 1,  0), ( 2,  0), ( 3,  0)),

    # diagonal
    ((-3, -3), (-2, -2), (-1, -1)),
    ((-2, -2), (-1, -1), ( 1,  1)),
    ((-1, -1), ( 1,  1), ( 2,  2)),
    (( 1,  1), ( 2,  2), ( 3,  3)),        
    ((-3,  3), (-2,  2), (-1,  1)),
    ((-2,  2), (-1,  1), ( 1, -1)),
    ((-1,  1), ( 1, -1), ( 2, -2)),
    (( 1, -1), ( 2, -2), ( 3, -3)),                
)


def display(board):
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


def play(col,board,player):
    board[col-1].append(player)
    display(board)
  

def winning_move(board, col):
    current_col = col-1
    current_row = len(board[current_col])-1   
    current_player = board[current_col][current_row]
    for rule in WINNING_RULES:
        try:
            for relative_col, relative_row in rule:
                other_col = current_col+relative_col
                other_row = current_row+relative_row

                if other_col < 0 or other_row < 0:
                    raise IndexError

                if board[other_col][other_row] != current_player:
                    break
            else:
                return True
        except IndexError:
            pass
    
    return False


def run():
    board = [[], [], [], [], [], [], []]
    player = 1
    os.system("clear")
    player_type= int(input("Do you to play vs a Robot (type out 1) or vs a human(you will play on the same computer)(type out 2)"))
    display(board)
    while True:    
        if player_type == 2:
            print("It's Player",player,"'s Turn")
            col = int(input("Which column do you want to play ?"))
        elif player_type == 1:
            print("Warning you will be destroy by my Terminator (diabolic laugh)") 
            if player == 1:
                print("It's Human Player Turn")
                col = int(input("Which column do you want to play ? Stupid human"))
            if player == 2:
                col = robot_testvalue(board,col)        
        play(col,board,player)

        if winning_move(board, col):
            print("gg, player",player,"You win !")
            break

        if player == 1:
            player = 2
        else:
            player = 1            
        
    
if __name__ == "__main__":
    run()
