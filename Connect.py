board= [[1],[],[],[],[],[],[]]
row= 6
col= 7

def display():
    print(" 1"," 2"," 3"," 4"," 5"," 6"," 7")
    print("╔══╦══╦══╦══╦══╦══╦══╗")
    diff = 5
    for c in range (row):
        print("║",end="")
        for r in range (col):
            try:
                print(board[r][c+diff],"║",end ="")
            except Exception as e:
                print(" ","║",end="")     
        print("")
        diff= diff-2
display()