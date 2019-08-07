# This problem was asked by Google.
# Given the root to a binary tree, implement serialize(root), 
# 	which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node_tree):
	if node_tree == None:
		return 'null'
	return '{"val": "' + node_tree.val + '","left":' + serialize(node_tree.left) + ',"right":' + serialize(node_tree.right) + '}'

def deserialize(node_string):
	if node_string == 'null':
		return None
	# Remove leading and trailing bracket
	node_string = node_string[1:-1]

	## Get value of current node
	node_val = node_string.split(',', 1)[0].split(':')[1]
	node_left_val_string = 'null'
	node_right_val_string = 'null'
	## Get value of current left
	# Remaining string contains current left and right
	remaining_string = node_string.split(',', 1)[1].split(':', 1)[1]
	print('Remaining string: ', remaining_string)
	# Isolating left node object if it exists
	if remaining_string.startswith('{'):
		bracket_counter = 1
		# Starts at one because of space at beginning of string
		char_index = 1
		while bracket_counter > 0:
			if remaining_string[char_index] == '{':
				bracket_counter += 1
			elif remaining_string[char_index] == '}':
				bracket_counter -= 1
			char_index += 1
		node_left_val_string = remaining_string[:char_index]
	# If doesn't exist, then check right node
	else:
		node_right_val_string = remaining_string.split(',', 1)[1].split(':', 1)[1]

	return Node(node_val, deserialize(node_left_val_string), deserialize(node_right_val_string))




root = Node('root')
node1 = Node('root', Node('left'), Node('right'))
node2 = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node2))
print(deserialize(serialize(node2)).left.left.val)