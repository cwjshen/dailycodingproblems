# This problem was asked by Google.

# Given an array of integers and a number k, where 1 <= k <= length of the array, 
# compute the maximum values of each subarray of length k.

# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. You can modify the input array in-place 
# and you do not need to store the results. You can simply print them out as you compute them.

# Also leetcode - 239. Sliding Window Maximum

def find_maximums(arr, k):
    curr_max = -1
    curr_second_max
    for i in range(k):
        if arr[i] > curr_max:
            curr_max = arr[i]
    for i in range(1, k):


    left_ptr = 0
    right_ptr = k-1

    while right_ptr < len(arr):
        print(curr_max)
        right_ptr += 1
        if arr[left_ptr] == curr_max:
            if arr[right_ptr] > arr[left_ptr]:
                curr_max = arr[right_ptr]
            else: