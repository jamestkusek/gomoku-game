import sys
import random
import pygame
from board import Board
import gui


GRID_SIZE = 15



def main():
    #gui.main_menu()
    gameplay()



def gameplay():
    gui.draw_game_board()
    board = Board()
    win = False
    current_player = 1
    while win == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if gui.mouse_in_grid(event.pos):

                    cell_id = gui.find_cell(event.pos)
                    indices = get_list_indices(cell_id)

                    if board.add_piece(current_player, indices):
                        gui.update_cell(current_player, cell_id)
                        if board.check_win(indices):
                            win = True
                        if current_player == 1:
                            current_player = 2
                        else:
                            current_player = 1
                    else:
                        print("cell already occupied")

    print("Player " + str(current_player) + " wins !")
    gui.draw_game_board()
    #gui.end_game_menu()




def get_list_indices(cell_id):
    column = (cell_id % (GRID_SIZE))
    row = cell_id // GRID_SIZE
    return column,row
main()



