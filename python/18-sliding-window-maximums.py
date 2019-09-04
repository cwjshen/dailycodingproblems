# This problem was asked by Google.

# Given an array of integers and a number k, where 1 <= k <= length of the array, 
# compute the maximum values of each subarray of length k.

# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. You can modify the input array in-place 
# and you do not need to store the results. You can simply print them solution as you compute them.

# Also leetcode - 239. Sliding Window Maximum

from collections import deque

def find_maximums(arr, k):
    # In plain english, we define a deque saying that for a given window, whatever is at the 
    #   the front of this deque will be the maximum for that window
    deq = deque()
    solution = []
    for i, num in enumerate(arr): 
        # Remove all indices with values smaller than current iteration value  
        while deq and arr[deq[-1]] < num:
            deq.pop()
        deq.append(i)

        if deq[0] == i - k:
            deq.popleft()
        # We only need to start appending to our solution once we get to window size
        if i >= k - 1:
            # Add to solution whatever is at the front of the deque
            solution.append(arr[deq[0]])
        print(deq, solution)
    return solution

find_maximums([10, 5, 2, 7, 8, 7], 3)
# find_maximums([10, 5, 2, 7, 6, 5, 4, 6, 5], 3)