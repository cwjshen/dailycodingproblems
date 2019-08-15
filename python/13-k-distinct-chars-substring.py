# This problem was asked by Amazon.
# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

def k_dist_chars(s, k):
    if k == 0:
        return 0

    curr_longest_word = ''
    char_dict = {}

    left_ptr = 0
    right_ptr = 0

    while right_ptr < len(s):
        if s[right_ptr] not in char_dict:
            char_dict[s[right_ptr]] = 1
        else:
            char_dict[s[right_ptr]] += 1

        while len(char_dict.keys()) > k:
            char_dict[s[left_ptr]] -= 1
            if char_dict[s[left_ptr]] == 0:
                del char_dict[s[left_ptr]]
            left_ptr += 1

        if right_ptr - left_ptr + 1 > len(curr_longest_word):
            curr_longest_word = s[left_ptr:right_ptr+1]
        right_ptr += 1
    print(curr_longest_word)
    return len(curr_longest_word)

print(k_dist_chars('abcddddeaaaffgggekairkf', 3))