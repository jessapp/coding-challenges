"""
In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?

Example:
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
Explanation: 
The grid is:
[ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]
"""

def maxIncreaseKeepingSkyline(grid):
    num_rows = len(grid)
    new_grid = []
    
    top_bottom_skyline = []
    left_right_skyline = []
    
    for horizontal_line in grid:
        current_max = 0
        max_index = 0
        for index, num in enumerate(horizontal_line):
            if num > current_max:
                current_max = num
                max_index = index 
        left_right_skyline.append(current_max)
                
                
    for i in range(num_rows):
        top_bottom_current_max = 0
        top_bottom_max_index = 0
        for index, horizontal_line in enumerate(grid):
            num = horizontal_line[i]
            if num > top_bottom_current_max:
                top_bottom_current_max = num
                top_bottom_max_index = index
        top_bottom_skyline.append(top_bottom_current_max)

    for i in range(num_rows):
        new_row = []
        for j in range(num_rows):
            i_constraint = left_right_skyline[i]
            j_constraint = top_bottom_skyline[j]
            new_value = min(i_constraint, j_constraint)
            new_row.append(new_value)
        new_grid.append(new_row)

    total = 0
                
    for i in range(num_rows):
        for j in range(num_rows):
            old_val = grid[i][j]
            new_val = new_grid[i][j]
            increase = new_val - old_val
            total += increase
    return total
                
    print(total)