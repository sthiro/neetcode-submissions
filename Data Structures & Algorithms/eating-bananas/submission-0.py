# Here k is bananas-per-hour eating rate
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_bananas = max(piles)
        k_possibilities = list(range(1, max_bananas + 1)) # 1 to max banana number range is the possibility of K
        
        return find_min_k(piles, k_possibilities, h)
        # print(calculate_time(piles, 2))

        
def find_min_k(piles: List[int], k_possibilities: List[int], target_time: int) -> int:
    l0, h0 = 0, len(k_possibilities) - 1
    k_mid_pos = 0 # initializing

    print(f"Input: {piles}, Target {target_time}")
    while h0 - l0 >= 0: 
        print("")

        k_mid_num_old = k_possibilities[k_mid_pos] # This variable is used in while loop else part
        k_mid_pos = (l0 + h0) // 2 # Finding Mid positiion
        k_mid_num = k_possibilities[k_mid_pos]


        time = calculate_time(piles, k_mid_num)
        print(f"k_possibilities: {k_possibilities[l0:h0+1]}")
        print(f"k mid pos: {k_mid_pos}, k_mid_num: {k_mid_num}, time={time}")

        if time == target_time: return k_mid_num
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
        print("\nEntered Else part\n")
        print(f"k_possibilities: {k_possibilities[l0:h0+1]}")
        print(f"target_time {target_time} actual time {time}")
        print(f"k_mid_num_old {k_mid_num_old}, k_mid_num {k_mid_num}")

        if time > target_time: return k_mid_num_old # return previous k value
        else: return k_mid_num # return lasst k value  

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
