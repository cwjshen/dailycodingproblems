# This problem was asked by Uber.
# Given an array of integers, return a new array such 
# 	that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], 
# 	the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

array1 = [1, 2, 3, 4, 5]
array2 = [3, 2, 1]
array3 = [1, 2, 3, 4]
array4 = [1, 2]

# O(n) time
# One pass to get total product
# One more pass to get each output
def WithDivision(arr):
	running_product = 1
	for number in arr:
		running_product = running_product * number
	return [running_product / i for i in arr]


# 1,2,3,4,5
# Two intermediate lists:
# O(2N) -> O(N)
# {1}, 1*1, 1*2, 1*2*3, 1*2*3*4
# 5*4*3*2, 5*4*3, 5*4, 5, {1} 
# {1} - these are placeholder 1s

# Then multiply through index-wise
# O(N)

def NoDivision(arr):
	running_product_ltr = 1
	running_product_rtl = 1

	solution_list = []
	left_to_right = [1]
	right_to_left = [1]
	
	for number in arr[0:len(arr)- 1]:
		running_product_ltr = running_product_ltr * number
		left_to_right.append(running_product_ltr)
	arr.reverse()
	
	for number in arr[0:len(arr) - 1]:
		running_product_rtl = running_product_rtl * number
		right_to_left.insert(0, running_product_rtl)
	
	print('LtoR: ', left_to_right)
	print('RtoL: ', right_to_left)

	for i in range(len(arr)):
		solution_list.append(left_to_right[i] * right_to_left[i])
	return solution_list


# print(WithDivision(array1))
# print(WithDivision(array2))
print(NoDivision(array1))
# print(NoDivision(array2))
# print(NoDivision(array3))
# print(NoDivision(array4))