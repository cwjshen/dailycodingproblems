# This problem was asked by Microsoft.
# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. 
#   If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.
# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", 
#   you should return ['the', 'quick', 'brown', 'fox'].
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", 
#   return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

word_set = ['the', 'quick', 'brown', 'fox']
sentence = "thequickbrownfox"

word_set2 = ['the', 'they', 'then']
sentence2 = 'thentheythe'

word_set3 = ['bed', 'bath', 'bedbath', 'and', 'beyond']
sentence3 = 'bedbathandbeyond'

def reconstruct_sentence(sentence, word_set):
    solution = []
    # While we have remaining words to find in our sentence
    while sentence:
        for word in word_set:
            # if sentence starts with current word and the remaining sentence is valid
            if sentence.startswith(word) and is_valid(sentence[len(word):], word_set):
                solution.append(word)
                sentence = sentence[len(word):]

    return solution

def is_valid(sentence, word_set):
    # if we successfully find the last word in the sentence, our next substring will be empty and we should return true when we check 
    #   if this empty substring is valid
    if not sentence:
        return True
    for word in word_set:
        if sentence.startswith(word):
            return True

print(reconstruct_sentence(sentence2, word_set2))