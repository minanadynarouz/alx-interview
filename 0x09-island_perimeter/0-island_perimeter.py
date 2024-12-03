#!/usr/bin/python3
"""Defines island perimeter finding function."""


def island_perimeter(grid):
    """Return the perimiter of an island.
    The grid represents water by 0 and land by 1.
    Args:
        grid (list): A list of list of integers representing an island.
    Returns:
        The perimeter of the island defined in grid.
    """
    
    w = 0
    h = 0

    first_width_index = 0
    last_width_index = 0

    top_height_index = 0
    last_height_index = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                first_width_index = j
                top_height_index = i
                break
        
        for j in range(len(grid[0]) - 1, -1, -1):
            if grid[i][j] == 1:
                last_width_index = j
                break
        
        if (last_width_index - first_width_index) + 1 > w:
            w = (last_width_index - first_width_index) + 1

    for i in range(len(grid) - 1, -1, -1):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                last_height_index = i
                break

    h = (top_height_index - last_height_index) + 1

    return (w + w + h + h)