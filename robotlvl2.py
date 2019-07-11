import random


def robot_testvalue(board,col):
    boardscore = []
    boardtest = board
    for i in range(7):
        score = 0
        boardtest[i].append(2)
        heighttest = len(board[i])-1
        if len(board[i]) > 5:
            score = 0
        else:
            #tests 1pt puis 2pt ect jusque 5pt
            #1point (1 jeton aligné mais dans le tableau)
            score = 1
            
            
            #2points(aligne 2 jetons)
            #horizontal
            try:
                if boardtest[i-1][heighttest] == boardtest[i][heighttest]:        
                    score=2
            except IndexError:
                pass
            try:
                if boardtest[i][heighttest] == boardtest[i+1][heighttest]:        
                    score=2
            except IndexError:
                pass
            #vertical
            try:
                if boardtest[i][heighttest] == boardtest[i][heighttest-1]:        
                    score=2
            except IndexError:
                pass
            #diagonale croissante
            try:
                if boardtest[i-1][heighttest-1] == boardtest[i][heighttest]:        
                    score=2
            except IndexError:
                pass
            try:
                if boardtest[i][heighttest] == boardtest[i+1][heighttest+1]:        
                    score=2
            except IndexError:
                pass
            #diagonale décroissante
            try:
                if boardtest[i-1][heighttest+1] == boardtest[i][heighttest]:        
                    score=2
            except IndexError:
                pass
            try:
                if boardtest[i][heighttest] == boardtest[i+1][heighttest-1]:        
                    score=2
            except IndexError:
                pass
     
     
            #3points (aligne 3 jetons)
            #horizontal
            try:
                if boardtest[i][heighttest] == boardtest[i+1][heighttest] == boardtest[i+2][heighttest]:
                    score = 3
            except IndexError :
                pass
            try:
                if boardtest[i-1][heighttest] == boardtest[i][heighttest] == boardtest[i+1][heighttest]:
                    score = 3
            except IndexError :
                pass
            try:
                if boardtest[i-2][heighttest] == boardtest[i-1][heighttest] == boardtest[i][heighttest]:
                    score = 3
            except IndexError :
                pass
            #vertical
            try:
                if boardtest[i][heighttest] == boardtest[i][heighttest-1] == boardtest[i][heighttest-2]:
                    score = 3
            except IndexError :
                pass
            #diagonale croissante
            try:
                if boardtest[i][heighttest] == boardtest[i+1][heighttest+1] == boardtest[i+2][heighttest+2]:
                    score = 3
            except IndexError :
                pass
            try:
                if boardtest[i-1][heighttest-1] == boardtest[i][heighttest] == boardtest[i+1][heighttest+1]:
                    score = 3
            except IndexError :
                pass
            try:
                if boardtest[i-2][heighttest-2] == boardtest[i-1][heighttest-1] == boardtest[i][heighttest]:
                    score = 3
            except IndexError :
                pass
            #diagonale décroissante
            try:
                if boardtest[i][heighttest] == boardtest[i+1][heighttest-1] == boardtest[i+2][heighttest-2]:
                    score = 3
            except IndexError :
                pass
            try:
                if boardtest[i-1][heighttest+1] == boardtest[i][heighttest] == boardtest[i+1][heighttest-1]:
                    score = 3
            except IndexError :
                pass
            try:
                if boardtest[i-2][heighttest+2] == boardtest[i-1][heighttest-1] == boardtest[i][heighttest]:
                    score = 3
            except IndexError :
                pass
            
     
            #4pt (contre puissance 4)
            #horizontale
            try:
                if boardtest[i][heighttest] != boardtest[i+1][heighttest] and boardtest[i+1][heighttest] == boardtest[i+2][heighttest] == boardtest[i+3][heighttest]:
                    score = 4
            except IndexError:
                pass
            try:
                if boardtest[i][heighttest] != boardtest[i-1][heighttest] and boardtest[i-1][heighttest] == boardtest[i+1][heighttest] == boardtest[i+2][heighttest]:
                    score = 4
            except IndexError:
                pass
            try:
                if boardtest[i][heighttest] != boardtest[i-2][heighttest] and boardtest[i-2][heighttest] == boardtest[i-1][heighttest]== boardtest[i+1][heighttest]:
                    score = 4
            except IndexError:
                pass
            try:
                if boardtest[i-3][heighttest] == boardtest[i-2][heighttest] == boardtest[i-1][heighttest] and boardtest[i-1][heighttest] != boardtest[i][heighttest]:
                    score = 4
            except IndexError :
                pass
            #verticale
            try:
                if boardtest[i][heighttest] != boardtest[i][heighttest-1] and boardtest[i][heighttest-1] == boardtest[i][heighttest-2] == boardtest[i][heighttest-3]:
                    score = 4
            except IndexError:
                pass
            #diagonale croissante
            try:
                if boardtest[i][heighttest] != boardtest[i+1][heighttest+1] and boardtest[i+1][heighttest+1] == boardtest[i+2][heighttest+2] == boardtest[i+3][heighttest+3]:
                    score = 4
            except IndexError:
                pass
            try:
                if boardtest[i][heighttest] != boardtest[i-1][heighttest-1] and boardtest[i-1][heighttest-1] == boardtest[i+1][heighttest+1] == boardtest[i+2][heighttest+2]:
                    score = 4
            except IndexError:
                pass
            try:
                if boardtest[i][heighttest] != boardtest[i-2][heighttest-2] and boardtest[i-2][heighttest-2] == boardtest[i-1][heighttest-1] == boardtest[i+1][heighttest+1]:
                    score = 4
            except IndexError:
                pass
            try:
                if boardtest[i][heighttest] != boardtest[i-3][heighttest-3] and boardtest[i-3][heighttest-3] == boardtest[i-2][heighttest-2] == boardtest[i-1][heighttest-1]:
                    score = 4
            except IndexError:
                pass
            #diagonale décroissante
            try:
                if boardtest[i][heighttest] != boardtest[i-1][heighttest+1] and boardtest[i-1][heighttest+1] == boardtest[i-2][heighttest+2] == boardtest[i-3][heighttest+3]:
                    score = 4
            except IndexError:
                pass
            try:
                if boardtest[i][heighttest] != boardtest[i+1][heighttest-1] and boardtest[i+1][heighttest-1] == boardtest[i-1][heighttest+1] == boardtest[i-2][heighttest+2]:
                    score = 4
            except IndexError:
                pass
            try:
                if boardtest[i][heighttest] != boardtest[i+2][heighttest-2] and boardtest[i+2][heighttest-2] == boardtest[i+1][heighttest-1] == boardtest[i-1][heighttest+1]:
                    score = 4
            except IndexError:
                pass
            try:
                if boardtest[i][heighttest] == boardtest[i+3][heighttest-3] == boardtest[i+2][heighttest-2] == boardtest[i+1][heighttest-1]:
                    score = 4
            except IndexError:
                pass
            
            
            #5pt (victoire)
            #horizontale
            try:
                if boardtest[i][heighttest] == boardtest[i+1][heighttest] == boardtest[i+2][heighttest] == boardtest[i+3][heighttest]:
                    score = 5
            except IndexError:
                pass
            try:
                if boardtest[i-1][heighttest] == boardtest[i][heighttest] == boardtest[i+1][heighttest] == boardtest[i+2][heighttest]:
                    score = 5
            except IndexError:
                pass
            try:
                if boardtest[i-2][heighttest] == boardtest[i-1][heighttest] == boardtest[i][heighttest] == boardtest[i+1][heighttest]:
                    score = 5
            except IndexError:
                pass
            try:
                if boardtest[i-3][heighttest] == boardtest[i-2][heighttest] == boardtest[i-1][heighttest] == boardtest[i][heighttest]:
                    score = 5
            except IndexError :
                pass
            #verticale
            try:
                if boardtest[i][heighttest] == boardtest[i][heighttest-1] == boardtest[i][heighttest-2] == boardtest[i][heighttest-3]:
                    score = 5
            except IndexError:
                pass
            #diagonale croissante
            try:
                if boardtest[i][heighttest] == boardtest[i+1][heighttest+1] == boardtest[i+2][heighttest+2] == boardtest[i+3][heighttest+3]:
                    score = 5
            except IndexError:
                pass
            try:
                if boardtest[i-1][heighttest-1] == boardtest[i][heighttest] == boardtest[i+1][heighttest+1] == boardtest[i+2][heighttest+2]:
                    score = 5
            except IndexError:
                pass
            try:
                if boardtest[i-2][heighttest-2] == boardtest[i-1][heighttest-1] == boardtest[i][heighttest] == boardtest[i+1][heighttest+1]:
                    score = 5
            except IndexError:
                pass
            try:
                if boardtest[i-3][heighttest-3] == boardtest[i-2][heighttest-2] == boardtest[i-1][heighttest-1] == boardtest[i][heighttest]:
                    score = 5
            except IndexError:
                pass
            #diagonale décroissante
            try:
                if boardtest[i][heighttest] == boardtest[i-1][heighttest+1] == boardtest[i-2][heighttest+2] == boardtest[i-3][heighttest+3]:
                    score = 5
            except IndexError:
                pass
            try:
                if boardtest[i+1][heighttest-1] == boardtest[i][heighttest] == boardtest[i-1][heighttest+1] == boardtest[i-2][heighttest+2]:
                    score = 5
            except IndexError:
                pass
            try:
                if boardtest[i+2][heighttest-2] == boardtest[i+1][heighttest-1] == boardtest[i][heighttest] == boardtest[i-1][heighttest+1]:
                    score = 5
            except IndexError:
                pass
            try:
                if boardtest[i+3][heighttest-3] == boardtest[i+2][heighttest-2] == boardtest[i+1][heighttest-1] == boardtest[i][heighttest]:
                    score = 5
            except IndexError:
                pass
        del boardtest[i][-1]
        boardscore.append(score)
    
        print(score)
    
        

if __name__ == "__main__":
    robot_testvalue(board,col)