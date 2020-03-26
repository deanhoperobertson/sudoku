import numpy as np
import pandas as pd

ONE_NINE_SET = set(range(1,10))

inp = np.array([
    [0,0,7, 5,0,9, 0,3,0], 
    [0,8,9, 0,2,0, 0,0,6], 
    [0,1,0, 8,0,6, 9,7,0],
    
    [7,0,5, 0,6,0, 0,8,0],
    [0,0,8, 9,0,5, 6,0,0],
    [0,6,0, 0,1,8, 0,0,9],
    
    [0,7,0, 0,0,0, 0,1,0],
    [8,0,0, 0,5,0, 2,9,0],
    [0,5,0, 1,0,2, 4,0,7]
])

def get_quadrant(grid, x, y):
    x_start, y_start = 3*(x//3), 3*(y//3)
    x_end, y_end = x_start + 3, y_start + 3
    return grid[y_start:y_end,x_start:x_end]


def solve_sudoku(grid):  # no logic checks, simple elimination on lines + quadrant
    grid = np.copy(grid)
    while 0 in grid:
        for y, x in zip(*np.where(grid==0)):
            quadrant = get_quadrant(grid, x, y)
            known = set(grid[y,:]) | set(grid[:,x]) | set(quadrant.flatten())
            possibilities = list(ONE_NINE_SET - known)
            if len(possibilities) == 1:
                grid[y,x] = possibilities[0]
    return grid

solved_grid = solve_sudoku(inp)
print(solved_grid)