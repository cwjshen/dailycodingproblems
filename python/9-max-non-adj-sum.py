# This problem was asked by Airbnb.
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?

# [5, 1, 1, 5]

# start with 5
# if we include 5 -> inc sum is 5
# if we exclude 5 -> exc sum is 0

# look at 1
# if we include 1, we exclude previous, add 1 to exc sum of previous, update include sum -> 1+0 = 1
# if we exclude 1, exclude sum is previous include sum = 5

# look at 1
# if we include 1, we exclude previous, add 1 to exclude sum of previous, update include sum -> 5+1 = 6
# if we exclude 1, exclude sum is the larger of previous include sum and previous include sum = max(1,5) = 5

# look at 5
# if we include 1, we exclude previous, add 5 to previous exclude sum, update include sum -> 5 + 5 = 10
# if we exclude 5, exclude sum is larger of previous include sum and previous include sum = max(6,5) = 6

# at the end, return the larger of either include or exclude sum

def max_non_adj_sum(list):
    prev_include_sum = 0
    prev_exclude_sum = 0

    for num in list:
        curr_exclude_sum = max(prev_exclude_sum, prev_include_sum)
        
        # Update previous values for next iteration
        prev_include_sum = prev_exclude_sum + num # current include sum
        prev_exclude_sum = curr_exclude_sum

    return max(prev_exclude_sum, prev_include_sum)

print(max_non_adj_sum([2,1,-2,7,8,-10]))