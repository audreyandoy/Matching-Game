import numpy as np
from random import *

rows = 4
cols = 4
board = np.zeros((rows, cols, 2))
characters = [u'\u0293',u'\u0278',u'\u03C0',u'\u03A9',u'\u03A8',u'\u03A3',u'\u0414',u'\u0411']

def make_board():
    print("here")
    for i in range(2):
        for charid in range(len(characters)):
            r = randint(0, rows-1)
            c = randint(0, rows-1)
            while board[r,c,1] != 0.0:
                r = randint(0, rows-1)
                c = randint(0, rows-1)
            board[r,c,1] = charid

def print_board():
    print("    1 2 3 4")
    print("    -------")
    for r in range(rows):
        print('{} | '.format(r+1)+ ' '.join(characters[int(board[r,c,1])]
        if board[r,c,0] == 1.0 else u'\u2588' for c in range(cols)))

def get_choice(limit, pos, turn):
    while True:
        try:
            id = int(input('Enter the {} of the {} card you would like to flip:'.format(pos,turn)))-1
        except ValueError:
            print("That is not a number. Please enter a number between 1 and {}.".format(limit))
        else:
            if id >= limit:
                print('That {} is out of range. Please enter a number between 1 and {}.'.format(pos, limit))
            else:
                break
    return id

def main():
    make_board()
    print_board()

if __name__ == '__main__':
    main()   


