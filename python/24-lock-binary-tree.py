# This problem was asked by Google.

# Implement locking in a binary tree. A binary tree node can be locked or unlocked only if 
# all of its descendants or ancestors are not locked.

# Design a binary tree node class with the following methods:

# is_locked(), which returns whether the node is locked
# lock(), which attempts to lock the node. 
#   If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
# unlock(), which unlocks the node. 
#   If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
# You may augment the node to add parent pointers or any other property you would like. 
# You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. 
# Each method should run in O(h), where h is the height of the tree.

class Binary_Tree_Node:
    def __init__(self, val, parent=None, left=None, right=None, locked=False):
        self.val = val
        self.parent = parent
        self.left = left
        if left != None:
            left.parent = self
        self.right = right
        if right != None:
            right.parent = self
        self.locked = locked
        self.locked_descendants_count = 0

    def add_left(self, node):
        self.left = node
        node.parent = self

    def add_right(self, node):
        self.right = node
        node.parent = self

    def is_locked(self):
        return self.locked

    def lock(self):
        parent = self.parent
        # Check all ancestors to see if any are locked
        while parent != None:
            # If any ancestor is locked, return False
            if parent.is_locked():
                print('An ancestor is locked')
                return False
            parent = parent.parent

        # Check all descendants to see if any are locked   
        if any_descendants_locked_opt(self):
            print('A descendant is locked')
            return False 

        # If both checks passed, we can go ahead and lock the current node
        print('Locking node')
        self.locked = True

        # We go back and increment the locked descendant count of all the ancestors by 1
        parent = self.parent
        while parent != None:
            parent.locked_descendants_count += 1
            parent = parent.parent

        return True

    def unlock(self):
        parent = self.parent
        # Check all ancestors to see if any are locked
        while parent != None:
            # If any ancestor is locked, return False
            if parent.is_locked():
                print('An ancestor is locked')
                return False
            parent = parent.parent

        # Check all descendants to see if any are locked   
        if any_descendants_locked_opt(self):
            print('A descendant is locked')
            return False 

        # If both checks passed, we can go ahead and lock the current node
        print('Unlocking node')
        self.locked = False

        # We go back and decrement the locked descendant count of all the ancestors by 1
        parent = self.parent
        while parent != None:
            parent.locked_descendants_count -= 1
            parent = parent.parent

        return True

# INTUITIVE BRUTE FORCE DESCENDANTS CHECK
# Recursive helper function to check all descendants of a given node
# Returns True if any are locked
# Returns False if and only if none are locked
def any_descendants_locked(node):
    # If no descendants
    if node.left == None and node.right == None:
        return False
    # If left is None, check right
    if node.left == None:
        if node.right.is_locked():
            return True
        return any_descendants_locked(node.right)
    # If right is None, check left
    if node.right == None:
        if node.left.is_locked():
            return True
        return any_descendants_locked(node.left)
    # If left and right not None, check both        
    return any_descendants_locked(node.left) or any_descendants_locked(node.right)

def any_descendents_locked_opt(node):
    if node.locked_descendants_count > 0:
        return True
    return False

root = Binary_Tree_Node(val=0, locked=True)
left = Binary_Tree_Node(val=1, locked=False)
right = Binary_Tree_Node(val=2, locked=True)
left2 = Binary_Tree_Node(val=3, locked=False)

right.add_left(left2)
root.add_left(left)
root.add_right(right)
print(right.unlock())
