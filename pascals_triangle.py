"""
Given a non-negative integer numRows, generate the first numRows 
of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


def pascals_triangle(numRow):
    if numRows == 0 or not numRows:
            return []
        
        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return [[1], [1,1]]

        current_row = 3
        result = [[1], [1,1]]
        
        while current_row < (numRows + 1):
            last_row = result[-1]
            new_row = [last_row[0]]
            for i in range(1, len(last_row)):
                cur_num = last_row[i] + last_row[i-1]
                new_row.append(cur_num)
            new_row.append(last_row[-1])
            result.append(new_row)
            
            current_row += 1
            
        return result