class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return check_matrix(matrix, target)
     
        
def check_one_array(arr: list[int], target: int) -> bool: # Binary Search
    #Array in ascending order
    l0, h0 = 0, len(arr) - 1 #Initializing low and high pointers

    while l0 <= h0:
        mid_pos = (l0 + h0) // 2
        mid_num = arr[mid_pos]

        if mid_num == target: return True
        elif mid_num < target: # Right half
            # Leave h0 as it's
            l0 = mid_pos + 1
        else: # Left half
            # Leave l0 as it's
            h0 = mid_pos - 1
    else: return False # If there is no target value in given array

def check_matrix(matrix: List[List[int]], target: int) -> bool:
    for arr in matrix:
        if check_one_array(arr, target): #if there is target in given array
            return True
    else: return False # No target value in all individual array
        