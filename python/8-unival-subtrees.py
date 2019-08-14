# This problem was asked by Google.
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:

 #   0
 #  / \
 # 1   0
 #    / \
 #   1   0
 #  / \
 # 1   1

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_unival(node):

    # Base case - if node is None:
    if node == None:
        return True
    # Base case - if single leaf node
    elif (node.left == None and node.right == None):
        return True
    else:
        # Short circuit check for None first so we can evaluate node.left if None check is false
        while (node.left == None or node.left.val == node.val) and \
            (node.right == None or node.right.val == node.val):
            return is_unival(node.left) and is_unival(node.right)
        return False

def count_unival_subtrees(node):
    count = 0
    # Base case - if node is None
    if node == None:
        return 0
    # Base case - if current node is the root of a unival tree
    if is_unival(node):
        count += 1
    # Recurse through left and right and add to running count    
    count += count_unival_subtrees(node.left) + count_unival_subtrees(node.right)
    return count

left_leaf = Node(1, None, None)
right_leaf = Node(0, Node(1, Node(1, None, None), Node(1, None, None)), Node(0, None, None))
root_node = Node(0, left_leaf, right_leaf)

print(is_unival(root_node))
print(count_unival_subtrees(root_node))
print(count_unival_subtrees(Node(1, Node(1, None, None), Node(1, None, None))))

