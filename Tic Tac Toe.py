board = [[1, 2, 3], [4, 5, 6],[7, 8, 9]] #initializing my board with integers
from random import randrange

def display_board(board) :
    b=board[:] #in order not to get annoyed writing "board" many times
    print("\n+----------+----------+----------+\n|          |          |          |")
    print("| ",b[0][0],"|",b[0][1]," |",b[0][2]," |",sep="    ")
    print("|          |          |          |\n+----------+----------+----------+\n|          |          |          |")
    print("| ", b[1][0], "|", b[1][1], " |", b[1][2], " |", sep="    ")
    print("|          |          |          |\n+----------+----------+----------+\n|          |          |          |")
    print("| ", b[2][0], "|", b[2][1], " |", b[2][2], " |", sep="    ")
    print("|          |          |          |\n+----------+----------+----------+")

def list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for column in range(3):
            if board[row][column] not in ["o","X"]:
                free_fields.append((row, column))
    return free_fields 


def victory(board):
    b=board[:]
    if b[0][0] == "X" and b[0][1] == "X" and b[0][2] == "X" or \
       b[1][0] == "X" and b[1][1] == "X" and b[1][2] == "X" or \
       b[2][0] == "X" and b[2][1] == "X" and b[2][2] == "X" or \
       b[0][0] == "X" and b[1][0] == "X" and b[2][0] == "X" or \
       b[0][1] == "X" and b[1][1] == "X" and b[2][1] == "X" or \
       b[0][2] == "X" and b[1][2] == "X" and b[2][2] == "X" or \
       b[0][0] == "X" and b[1][1] == "X" and b[2][2] == "X" or \
       b[2][0] == "X" and b[1][1] == "X" and b[0][2] == "X":
        return "lost"
    elif b[0][0] == "o" and b[0][1] == "o" and b[0][2] == "o" or \
       b[1][0] == "o" and b[1][1] == "o" and b[1][2] == "o" or \
       b[2][0] == "o" and b[2][1] == "o" and b[2][2] == "o" or \
       b[0][0] == "o" and b[1][0] == "o" and b[2][0] == "o" or \
       b[0][1] == "o" and b[1][1] == "o" and b[2][1] == "o" or \
       b[0][2] == "o" and b[1][2] == "o" and b[2][2] == "o" or \
       b[0][0] == "o" and b[1][1] == "o" and b[2][2] == "o" or \
       b[2][0] == "o" and b[1][1] == "o" and b[0][2] == "o":
        return "won"
    else: return "tie"

def enter_move (board): #regulates the move of the user
    a = 0
    move = int(input("Enter your move\t"))
    while True:
        if move > 0 and move < 10:
            for row in range(3):
                for column in range(3):
                    if board[row][column] == move:
                        board[row][column] = "o"
                        display_board(board)
                        a += 1
                        return
            if a == 0:
                move = int(input("Make a valid move please\t"))
        else:
            move = int(input("Make a valid move please\t"))




def draw_move(board): #regulates the moves of the computer
    while True:
        move = randrange(1, 10)
        for row in range(3):
            for column in range(3):
                if board[row][column] == move:
                    board[row][column] = "X"
                    display_board(board)
                    return


print("LET'S START")
for i in range(1, 10):
    if i%2 == 1:
        draw_move(board)
        if victory(board) == "lost":
            print("\n\nYOU LOST MY MAN: Maybe next time :) ")
            break
        if victory(board) == "tie" and list_of_free_fields(board) == []:
            print("TIE")
            break
    else:
        enter_move(board)
        if victory(board) == "won":
            print("\n\nCONGRATS!! You won the computer ")
            break
        if victory(board) == "tie" and list_of_free_fields(board) == []:
            print("TIE :(")
            break




