#!/usr/bin/python3

def island_perimeter(grid):
    """
    The function calculates the perimeter of an island in a grid.
    A grid is considered an island if it consists of 1s only.
    """
    if len(grid) < 3 and isinstance(grid, list):
        return 0
    total_sum = 0
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j] == 1:
                sides_sum = grid[i][j - 1] + grid[i][j + 1] + (
                        grid[i - 1][j] + grid[i + 1][j])
                perimeter_sum = 4 - sides_sum
                if perimeter_sum == 4:
                    return 4
                else:
                    total_sum += perimeter_sum
    return total_sum
