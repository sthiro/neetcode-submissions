class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return target_finder(matrix, target)


def target_finder(matrix: List[List[int]], target: int) -> bool: # Binary Search
    #Array in ascending order , m x n
    x_len = len(matrix[0]) * len(matrix) # total length = m x n = mn
    l0, h0 = 0, x_len - 1 #I nitializing low and high pointers

    # Binary Search as it's 1D Sorted array 
    while l0 <= h0:
        mid_pos = (l0 + h0) // 2
        mid_num = mapper(matrix, mid_pos) #Finds middle num in mapped linear array

        if mid_num == target: return True
        elif mid_num < target: # Right half
            # Leave h0 as it's
            l0 = mid_pos + 1
        else: # Left half
            # Leave l0 as it's
            h0 = mid_pos - 1
    else: return False # If there is no target value in matrix

# Maps linear array position in matrix (helps to simulate matrix as normal 1D array)
def mapper(matrix: List[List[int]], linear_pos: int) -> int:
    # m x n = X x Y
    x_len = len(matrix[0]) # checking length of one row 
    x_axis_pos = linear_pos % x_len # x axis position in matrix
    y_axis_pos = linear_pos // x_len # y axis position or relevent single array in matrix
    linear_val = matrix[y_axis_pos][x_axis_pos]
    return linear_val