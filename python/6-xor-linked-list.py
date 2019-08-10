# This problem was asked by Google.

# An XOR linked list is a more memory efficient doubly linked list. 
# Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. 
# Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

# If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions 
# that converts between nodes and memory addresses.


# Important concepts:
# XOR - Bitwise exclusive OR operator: ^
# 1010 XOR 0101 = 1111
# The inverse operation is just the XOR of the other variable:
# A ^ B = C 
# A = C ^ B

class Node:
    def __init__(self, val, both=None):
        self.val = val
        self.both = both

class XORLinkedList:
	def __init__(self, head_ptr):
		self.head = head_ptr

	def print_ll(self):
		curr_node = dereference_pointer(self.head)
		while curr_node.both != None:
			print((curr_node.val, curr_node.both), end='->')
			curr_node = dereference_pointer(curr_node.both ^ get_pointer(curr_node))
		print((curr_node.val, curr_node.both))

	def add(self, Node):
		visited_addrs = set()
		curr_node = dereference_pointer(self.head)
		while curr_node.both != None:
			visited_addrs.add(get_pointer(curr_node))
			curr_node = dereference_pointer(curr_node.both ^ get_pointer(curr_node))

		visited_addrs.add(get_pointer(curr_node))	
		if get_pointer(Node) not in visited_addrs:
			curr_node.both = get_pointer(curr_node) ^ get_pointer(Node)
			print(Node.val, ' added')
		else:
			print(Node.val, ' already exists')
		

	def get(self, index):
		curr_node = dereference_pointer(self.head)
		if index == 0:
			return curr_node
		for i in range(1, index + 1):
			if curr_node.both == None:
				print('index out of list size range')
				return
			curr_node = curr_node = dereference_pointer(curr_node.both ^ get_pointer(curr_node))
		return curr_node			

my_nodes = [Node('a'), Node('b'), Node('c'), Node('d'), Node('e')]
my_addrs = [0, 1, 2, 3, 4]
nodes_to_addrs = dict(zip(my_nodes, my_addrs))
addrs_to_nodes = dict(zip(my_addrs, my_nodes))

# Implement method to mock the retrieval of pointer for a node
def get_pointer(Node):
	return nodes_to_addrs[Node]

def dereference_pointer(ptr):
	return addrs_to_nodes[ptr]

xor_linked_list = XORLinkedList(get_pointer(my_nodes[0]))
xor_linked_list.add(my_nodes[1])
xor_linked_list.add(my_nodes[2])
xor_linked_list.add(my_nodes[3])
xor_linked_list.add(my_nodes[4])



xor_linked_list.print_ll()
print(xor_linked_list.get(4))
# print(dereference_pointer(xor_linked_list.head).val)
# print(dereference_pointer(dereference_pointer(xor_linked_list.head).both ^ get_pointer(dereference_pointer(xor_linked_list.head))).val)