# <-- Plan
"""
Generate new board

Generate 2 '2' s in random locations in grid

move
    move all boxes in specified direction
    merge boxes of the same type
        resultant box is sum of boxes
    generate 1 '2'  in a random unoccupied location


"""
import sys
from random import choice
from time import sleep
import pygame

def clear_screen(msg=None):
    if msg:
        print(msg)
    sleep(DELAY)
    print("\033[H\033[J", end="")


def reset_board():
    return [[None for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]


def print_board(board):
    """
    Print neatly formatted board
    """
    print('_'*24)
    for i in board:
        for j in i:
            if j is None:
                print(f"|    |", end='')
            else:
                print(f"|{j:^4}|", end='')
        print()
    print('_' * 24)


def add_two(board):
    # print_board(board)
    # find an unoccupied space
    x_coords, y_coords = [], []
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if board[y][x] is None:
                x_coords.append(x)
                y_coords.append(y)
    if len(x_coords) == 0 or len(y_coords) == 0:
        sys.exit("Game over")
    else:
        x = choice(x_coords)
        y = choice(y_coords)
        board[y][x] = 2
        # print(board)
        # print_board(board)

        return board


def check_if_full(board):
    global gameover
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if board[y][x] is not None:
                gameover = True



def move(direction, board):
    """algorithm for movement is compress merge compress"""
    if direction == 'a':
        for row in range(len(board)):
            # print(board[row])
            # Compress 1
            new_row = []
            for cell in board[row]:
                if cell is not None:
                    new_row.append(cell)
            while len(new_row) != BOARD_WIDTH:
                new_row.append(None)

            # Merge
            for x in range(1, len(new_row)):
                # print(new_row[x])
                if new_row[x-1] == new_row[x] and new_row[x] is not None:
                    new_row[x-1] = new_row[x]*2
                    new_row[x] = None

            board[row] = new_row

            # Compress 2
            new_row = []
            for cell in board[row]:
                if cell is not None:
                    new_row.append(cell)
            while len(new_row) != BOARD_WIDTH:
                new_row.append(None)

            board[row] = new_row
    if direction == 'd':
        for row in range(len(board)):
            # print(board[row])
            # Compress 1
            new_row = []
            for cell in board[row]:
                if cell is not None:
                    new_row.append(cell)
            while len(new_row) != BOARD_WIDTH:
                new_row =  [None] + new_row
            # print(f"\tNew row, after compression 1 {new_row}")

            # Merge
            # print([x for x in range(len(new_row)-1, 0, -1)])
            for x in range(len(new_row)-1, 0, -1):
                # print(new_row[x])
                if new_row[x - 1] == new_row[x] and new_row[x] is not None:
                    new_row[x - 1] = None
                    new_row[x] = new_row[x] * 2

            board[row] = new_row

            # Compress 2
            new_row = []
            for cell in board[row]:
                if cell is not None:
                    new_row.append(cell)
            while len(new_row) != BOARD_WIDTH:
                new_row =  [None] + new_row

            board[row] = new_row

    if direction == 'w':

        # print(board)
        cols = {}
        for row in board:
            for x in range(len(row)):
                if x not in cols.keys():
                    cols[x] = []
                cols[x].append(row[x])
        # print(cols)
        # print()
        for x in cols:
            # Essentially converting columns into a state I can treat like rows
            # Compression 1
            # print("Compression 1\tColumn ", x)
            # print(cols[x])
            temp = []
            for cell in cols[x]:
                if cell is not None:
                    temp.append(cell)
            while len(temp) != len(cols[x]):
                temp = temp + [None]
            cols[x] = temp
            # print(cols[x])
            # print()

            # Merge
            # print(temp)
            for i in range(1, len(temp)):
                # print(new_row[x])
                if temp[i - 1] == temp[i] and temp[i] is not None:
                    temp[i - 1] = temp[i] * 2
                    temp[i] = None

            cols[x] = temp

            # Compression 2
            # print("Compression 2\tColumn ", x)
            # print(cols[x])
            temp = []
            for cell in cols[x]:
                if cell is not None:
                    temp.append(cell)
            while len(temp) != len(cols[x]):
                temp = temp + [None]
            cols[x] = temp
            # print(cols[x])
            # print()

        # write new columns back to board
        for y in range(len(board)):
            for x in range(len(board[y])):
                board[y][x] = cols[x][y]

    if direction == 's':

        # print(board)
        cols = {}
        for row in board:
            for x in range(len(row)):
                if x not in cols.keys():
                    cols[x] = []
                cols[x].append(row[x])
        # print(cols)
        # print()
        for x in cols:
            # Essentially converting columns into a state I can treat like rows
            # Compression 1
            # print("Compression 1\tColumn ", x)
            # print(cols[x])
            temp = []
            for cell in cols[x]:
                if cell is not None:
                    temp.append(cell)
            while len(temp) != len(cols[x]):
                temp = [None] + temp
            cols[x] = temp
            # print(cols[x])
            # print()

            # Merge
            # print(temp)
            for i in range(len(temp)-1, 0, -1):
                # print(new_row[x])
                if temp[i - 1] == temp[i] and temp[i] is not None:
                    temp[i - 1] = None
                    temp[i] = temp[i] * 2

            cols[x] = temp

            # Compression 2
            # print("Compression 2\tColumn ", x)
            # print(cols[x])
            temp = []
            for cell in cols[x]:
                if cell is not None:
                    temp.append(cell)
            while len(temp) != len(cols[x]):
                temp = [None] + temp
            cols[x] = temp
            # print(cols[x])
            # print()

        # write new columns back to board
        for y in range(len(board)):
            for x in range(len(board[y])):
                board[y][x] = cols[x][y]


    board = add_two(board)
    clear_screen()




def main():
    """
    board = reset_board()
    # print_board(board)
    # board = [[2, None, None, 2], [None, None, None, None], [2, None, None, None], [None, None, 2, None]]
    # board = add_two(board)
    # board = add_two(board)
    print_board(board)
    while not gameover:

        move_input = input("Enter a move, (wasd):\t").lower().strip()
        if move_input == 'q':
            sys.exit("Closing the game...")
        move(move_input.strip().lower(), board)

        board = add_two(board)
        print_board(board)
    """
    running = True
    board = reset_board()
    print_board(board)

    while running:
        # Process events
        direction = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = not running
                pygame.quit()
                sys.exit()
        
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_w, pygame.K_UP]:
                    direction = 'w'
                if event.key in [pygame.K_s, pygame.K_DOWN]:
                    direction = 's'
                if event.key in [pygame.K_a, pygame.K_LEFT]:
                    direction = 'a'
                if event.key in [pygame.K_d, pygame.K_RIGHT]:
                    direction = 'd'

        # Game logic
        if direction:
            move(direction, board)
            
            print_board(board)

        # Maintaining timing
        pygame.time.Clock().tick(60)

    


BOARD_WIDTH = 4
BOARD_HEIGHT = 4
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500
DELAY = 0.25
gameover = False
# initialising pygame
pygame.init()

# setting up screen for pygame
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
if __name__ == '__main__':
    main()
