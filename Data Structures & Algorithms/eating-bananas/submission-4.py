# Here k is bananas-per-hour eating rate
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_bananas = max(piles)
        # 1 to max banana number range is the possibility of K
        
        return find_min_k(piles, max_bananas, h)
        
def find_min_k(piles: List[int], k_possibilities: int, target_time: int) -> int:
    l0, h0 = 1, k_possibilities 
    k_mid_pos = 0 # initializing

    while h0 - l0 >= 0: 
        k_mid_pos_old = k_mid_pos # This variable is used in while loop else part
        k_mid_pos = (l0 + h0) // 2 # Finding Mid positiion
        time = calculate_time(piles, k_mid_pos)

        if time == target_time: return k_mid_pos
        elif time < target_time:
            # Rate of eating is higher than expected value, so decrease the rate of eating
            # Check left half
            # Don't change the l0
            h0 = k_mid_pos - 1
            
        else: # Rate of eating is slower than expected value, so increase the rate of eating
            # Check right half
            # Don't change h0
            l0 = k_mid_pos + 1
    else: 

        if time > target_time: return k_mid_pos_old # return previous k value
        else: return k_mid_pos # return lasst k value  

def calculate_time(piles: List[int], k: int) -> int:
    # Two Cases
    # K > piles[i] or K < piles [i]

    #This for loop runs n times, where n is number of element in piles array

    total_time = 0
    for pile_bananas in piles:

        float_time = pile_bananas / k # Ex : float_time can be 3.0,3.2, 5
        # but it has to be integer
        # if int(float_time) < float_time <-- Ex: 3.0 < 3.2  .we need to make it 4
        if int(float_time) < float_time:
            total_time += int(float_time) + 1
        else: # int(float_time) = float_time <-- Ex: 0.0 = 0.0
            total_time += float_time 
        #print(f"float_time {float_time} total_time {total_time}")
    return total_time
