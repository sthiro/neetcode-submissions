# Here k is bananas-per-hour eating rate
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_bananas = max(piles)
        # 1 to max banana number range is the possibility of K
        
        return find_min_k(piles, max_bananas, h)
        
def find_min_k(piles: List[int], k_possibilities: int, target_time: int) -> int:
    l0, h0 = 1, k_possibilities 
    k_mid_pos = (l0 + h0) // 2 # initializing
    min_k = k_possibilities
    print(f"Target_time: {target_time}, piles: {piles}, h0: {h0}, lo: {l0}")

    while h0 >= l0: 
        print("")
        k_mid_pos = (l0 + h0) // 2 # Finding Mid positiion
        time = calculate_time(piles, k_mid_pos)
        print(f"l0: {l0}, h0: {h0}, time: {time}")
        print(f"k_mid_pos: {k_mid_pos}, time: {time}")

        if k_mid_pos < min_k and time <= target_time:
            min_k = k_mid_pos
            print("updating  min_k")
            print(f"min_k: {min_k}")


        if time <= target_time:
            # Rate of eating is higher than expected value, so decrease the rate of eating
            # Check left half
            # Don't change the l0
            h0 = k_mid_pos - 1
            
        else: # Rate of eating is slower than expected value, so increase the rate of eating
            # Check right half
            # Don't change h0
            l0 = k_mid_pos + 1
    else: 
        print("returned Else part")
        return min_k

def calculate_time(piles: List[int], k: int) -> int:
    # Two Cases
    # K > piles[i] or K < piles [i]

    #This for loop runs n times, where n is number of element in piles array

    time = 0
    for pile_bananas in piles:

        time += pile_bananas // k # Ex : float_time can be 3.0,3.2, 5
        modulas_time = pile_bananas % k

        if modulas_time > 0: time += 1
        
    return time