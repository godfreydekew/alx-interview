#!/usr/bin/python3
"""0. Island Perimeter"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island in a grid.
    :param grid: List of lists of integers (0 for water, 1 for land).
    :return: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                cell_perimeter = 4
                if r > 0 and grid[r - 1][c] == 1:
                    cell_perimeter -= 1
                if r < rows - 1 and grid[r + 1][c] == 1:
                    cell_perimeter -= 1
                if c > 0 and grid[r][c - 1] == 1:
                    cell_perimeter -= 1
                if c < cols - 1 and grid[r][c + 1] == 1:
                    cell_perimeter -= 1
                perimeter += cell_perimeter

    return perimeter
