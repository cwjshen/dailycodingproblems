# This problem was asked by Airbnb.
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?

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