# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

array1 = [10, 15, 3, 7]
array2 = [11, 15, 3, 7]
k = 17

# O(n^2) time
# Checks each number against every other number to see if sum exists
def BruteForce(arr, k):
	for i in range(len(arr)):
		for j in range(i + 1, len(arr)):
			if arr[i] + arr[j] == k:
				return True
	return False

# O(n) time
# Uses hash set to keep track of unique numbers seen
# On a single pass through the array:
# 	if sum complement exists in set, we've found the two numbers
#	else add current number to the set
# Lookup time for hash set is O(1)
def OnePass(arr, k):
	unique_seen = set()
	for number in arr:
		if k - number in unique_seen:
			return True
		else:
			unique_seen.add(number)
	return False

print(BruteForce(array1, 17))
print(OnePass(array1, 17))
