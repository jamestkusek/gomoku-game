import sys

GRID_SIZE = 15


class Board:
    def __init__(self):
        self.grid = [[0] * GRID_SIZE for x in range(GRID_SIZE)]
        self.grid_size = GRID_SIZE
        self.piece_count = 0

    # attempt to add a piece to the board, return True if piece added, False if piece already in cell
    def add_piece(self, player, indices):
        column = indices[0]
        row = indices[1]
        if self.grid[row][column] == 0:
            self.grid[row][column] = player
            self.piece_count += 1
            return True
        else:
            return False

    def check_win(self, indices):
        column = indices[0]
        row = indices[1]
        directions = [(1, 0), (0, 1), (1, -1), (-1, -1)]
        for dx, dy in directions:
            if (self.count_adjacent(dx, dy, column, row) + self.count_adjacent(-dx, -dy, column, row)) - 1 >= 5:

                return True
        return False


    def count_adjacent(self, dx, dy, column, row):
        piece = self.grid[row][column]
        count = 1
        x = column + dx
        y = row + dy

        while 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE and self.grid[y][x] == piece:
            count += 1
            print(count)
            x += dx
            y += dy
        return count
