# This problem was asked by Google.
# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
# In this example, assume nodes with the same value are the exact same node objects.
# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

    def print_remaining(self):
        node = self
        while node.nxt != None:
            node = node.nxt
            print(node.val, '->', end=" ")
        print("")

    def length(self):
        curr_node = self
        length = 1
        while curr_node.nxt != None:
            length += 1
            curr_node = curr_node.nxt
        return length

def get_intersecting_node(head_a, head_b):
    curr_a_node = head_a
    curr_b_node = head_b
    if head_a.length() > head_b.length():
        # Traverse up to where the two lengths are equal    
        curr_length = head_a.length()
        while curr_length > head_b.length():
            curr_a_node = curr_a_node.nxt
            curr_length -= 1
    elif head_b.length() > head_a.length():
        # if list b is larger, then just recall the method with b as the first arg
        get_intersecting_node(head_b, head_a)
    else:
        # if the two lists are the same length, then we can start searching for an intersection
                # Then traverse again up to where the two values are equal
        while curr_a_node.val != curr_b_node.val:
            curr_a_node = curr_a_node.nxt
            curr_b_node = curr_b_node.nxt

        print(curr_a_node.val)
        return curr_a_node.val

linked_list_a = Node(3, Node(7, Node(8, Node(10))))
linked_list_b = Node(99, Node(1, Node(8, Node(10))))
get_intersecting_node(linked_list_a, linked_list_b)