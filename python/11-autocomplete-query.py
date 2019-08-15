# This problem was asked by Twitter.
# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, 
#   return all strings in the set that have s as a prefix.
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

class Node:
    def __init__(self, val=None, children=None, is_end_of_a_word=False):
        self.val = val
        self.children = children if children != None else {}
        self.is_end_of_a_word = is_end_of_a_word

class Trie:
    def __init__(self, root=Node()):
        self.root = root

    def insert(self, string):
        curr_node = self.root
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(val=char)
            curr_node = curr_node.children[char]
        curr_node.is_end_of_a_word = True

    def find(self, string):
        curr_node = self.root
        for char in string:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return True

# We want to return a list of all words formed by the children
def process_children(node, prefix_string):
    solution_list = []
    # if node has no children, we assume that it is the end of a word and this traversed string to solution set
    # if we want, we can also just add a check to see if this node has the end-of-word flag set
    if node.children == None:
        return solution_list.append(prefix_string)
    else:
        if node.is_end_of_a_word:
            solution_list.append(prefix_string)
        for key in node.children:
            solution_list += process_children(node.children[key], prefix_string + node.children[key].val)
    return solution_list


def generate_trie(allowed_strings):
    # Preprocess dictionary of possible query strings into Trie
    my_trie = Trie()
    for word in allowed_strings:
        my_trie.insert(word)
    
    return my_trie 
       
def autocomplete(query_string, allowed_strings):

    my_trie = generate_trie(allowed_strings)

    curr_node = my_trie.root
    curr_word = query_string

    # Traverse to the point in the Trie where the query string ends
    for char in query_string:
        if char in curr_node.children:
            curr_node = curr_node.children[char]
        # if we aren't able to traverse to the end of the query string, 
        # it implies that no words exist that start with the query string
        # so we can return an empty result
        else:
            return []
    return process_children(curr_node, query_string)


def main():
    possible_words = [
        'test two',
        'testing',
        'shaan',
        'shaaning',
        'hello',
        'help',
        'helper',
        ''
    ]

    query_string = 'test'

    print(autocomplete(query_string, possible_words))

main()