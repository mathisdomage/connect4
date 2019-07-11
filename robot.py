import random


def robot_turn(board,col):    
    while True:
        col=random.randint(1,7)
        if len(board[col-1]) >= 6:
            pass
        else:
            break
    return col




















if __name__ == "__main__":
    robot_turn()