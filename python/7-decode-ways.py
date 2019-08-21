# This problem was asked by Facebook.
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.

# Leetcode 91 - decode ways

def numDecodings(string):
    if string[0] == '0':
        return 0
    if len(string) < 2:
        return 1
    else:
        a0 = 1
        a1 = 1
        for i in range(1, len(string)):
            # if consecutive pair is between 0 and 27 does not start with 0
            if 0 < int(string[i-1:i+1]) < 27 and string[i-1] != '0':
                # we can interpret the pair as individual digits or as a two digit number
                # so this is the sum of ways through n-2 and ways through n-1
                an = a0 + a1
            else:
                # we cannot interpret this pair as a two digit number, and is the same as the number of ways through n-1
                an = a1
            
            # if current digit is 0, then we invalidate the ways through n-1 because it would leave us with a trailing 0
            if string[i] == '0':
                an -= a1

            # increment your pointers tracking running sums
            a0 = a1
            a1 = an
        return an

print(numDecodings("01"))
print(numDecodings("12"))
print(numDecodings("123"))
print(numDecodings("1234"))
print(numDecodings("10"))
print(numDecodings("100"))