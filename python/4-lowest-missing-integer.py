# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.


# Test Cases
# [3, 4, -1, 1] -> 2
# [1, 2, 0] -> 3
# [-1] -> 1
# [0] -> 1
# [2] -> 1
# [5, 6] -> 1
# [-1, -1, -1, -1, 5] -> 1
# [3, 5] -> 1 or 4?

def lowest_missing_positive_int(arr):
	for i in range(len(arr)):
		while num_is_positive(arr, i) \
				and has_dest_index(arr, i) \
				and not is_in_correct_pos(arr, i) \
				and not spot_taken_by_duplicate(arr, i):

			# print('inwhile:', arr)
			swap(arr, i, arr[i] - 1)

	for i in range(len(arr)):
		if i != arr[i] - 1:
			return i + 1

	return len(arr) + 1


def swap(arr, a, b):
	arr[a], arr[b] = arr[b], arr[a]

def num_is_positive(arr, i):
	return arr[i] > 0

def has_dest_index(arr, i):
	return arr[i] - 1 < len(arr)

def is_in_correct_pos(arr, i):
	return arr[i] == i + 1

def spot_taken_by_duplicate(arr, i):
	return arr[i] == arr[arr[i] - 1]

arr1 = [3, 4, -1, 1] # 2
arr2 = [5, 3, 1, 2, 6, 8, 7] # 4
arr3 = [1, 2, 0] #3
arr4 = [-1] #1
arr5 = [5, 60] #1
arr6 = [2, 3, 1, 5, 6, 8, 7] #4
arr7 = [1, 2, 3, 4, 6, 7, 8, 10, 11, 12, 100] #5
arr8 = [8,9,2,4,5,6,1,3] #7
test_cases = [arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8]
for arr in test_cases:
	print(lowest_missing_positive_int(arr))
# print(lowest_missing_positive_int(arr2))