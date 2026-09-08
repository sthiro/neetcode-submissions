#[1, 2, 3, 4, 5, 6, 7, 8, 9]
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return find_num(nums, target)

def find_num(nums, target):
    h0, l0 = len(nums) - 1, 0 # Initializing Pointers

    while l0 <= h0:
        mid_pos = (l0 + h0) // 2 #finding middle pos relativie to given array
        middle_no = nums[mid_pos]
        print(f"middle_no: {middle_no}, mid_pos: {mid_pos}")

        if middle_no == target:
            return mid_pos #return position
        elif middle_no < target: #if target is in right half
            # leave h0 as it's before
            l0 = mid_pos + 1 # Change the h0 pointer next to mid_pos
        else: # if target is in left half
            # leave l0 as it's before
            h0 = mid_pos - 1

    else: return -1 # After finishing whole while loop and no target was found in the given array




