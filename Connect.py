board= [["O"],["X"],[],[],[],[],[]]

def display():
    print("╔═══╦═══╦═══╦═══╦═══╦═══╦═══╗")
    
    for c in range (5,-1,-1):
        print("║",end="")
        for r in range (7):
            try:
                print("",board[r][c],"║",end ="")
            except IndexError as e:
                print("  ","║",end="")     
        print("")
        if c > 0 :
            print("╠═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
        else:
            print("╚═══╩═══╩═══╩═══╩═══╩═══╩═══╝")
    print("  1   2   3   4   5   6   7")    
display()