# Given a 9 x 9 (2-dimensional array) and validate it. 


# Valid matrix


      # [ [5, 3, 4, 6, 7, 8, 9, 1, 2],
      #   [6, 7, 2, 1, 9, 5, 3, 4, 8],
      #   [1, 9, 8, 3, 4, 2, 5, 6, 7],
        
      #   [8, 5, 9, 7, 6, 1, 4, 2, 3],
      #   [4, 2, 6, 8, 5, 3, 7, 9, 1],
      #   [7, 1, 3, 9, 2, 4, 8, 5, 6],
        
      #   [9, 6, 1, 5, 3, 7, 2, 8, 4],
      #   [2, 8, 7, 4, 1, 9, 6, 3, 5],
      #   [3, 4, 5, 2, 8, 6, 1, 7, 9]]


def check_valid(nums):

    if nums is None:
        return False

    sorted_nums = sorted(nums)

    if len(sorted_nums) != 9:
        return False


    return sorted_nums == range(1, 10)


def validate_sudoku(board):

    # Check horizontally
    for line in board:
        if check_valid(line) == False:
            return False

    # Check vertically 

    for i in range(0, 9):
        new_array = []
        for line in board:
            new_array.append(line[i])

        if check_valid(new_array) == False:
            return False

    # Check 3 X 3

    groups = [board[:3], board[3:6], board[6:]]

    for group in groups:
        current_nums_1 = []
        current_nums_2 = []
        current_nums_3 = []
        for row in group:
            current_nums_1.extend(row[:3])
            current_nums_2.extend(row[3:6])
            current_nums_3.extend(row[6:])

        if check_valid(current_nums_1) == False:
            return False
        elif check_valid(current_nums_2) == False:
            return False
        elif check_valid(current_nums_3) == False:
            return False


    return True


print validate_sudoku([ [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 4, 1, 9, 5, 3, 2, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]])