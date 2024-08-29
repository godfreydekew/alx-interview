#!/usr/bin/python3

def island_perimeter(grid):
    """
    The function calculates the perimeter of an island in a grid.
    A grid is considered an island if it consists of 1s only.
    """
    if len(grid) < 3 and isinstance(grid, list):
        return 0
    total_sum = 0
    transposed_matrix = list(map(list, zip(*grid)))
    if (sum(grid[0]) + sum(grid[-1])) + sum(transposed_matrix[0]) + sum(transposed_matrix[-1]) == 0:
        for land in grid:
            total_sum += sum(land)
        return (total_sum * 2) + 2