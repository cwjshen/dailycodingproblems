# This problem was asked by Amazon.

# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
# Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2

# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?
# For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.


# Global caches
memo_dict = {1:1,2:2}
memo_dict_var = {}

def staircase_ways_rec(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return staircase_ways_rec(n-1) + staircase_ways_rec(n-2)

def staircase_ways_dp(n):
    if n < 1:
        return 0
    else:
        if n-2 not in memo_dict:
            memo_dict[n-2] = staircase_ways_dp(n-2)
        if n-1 not in memo_dict:
            memo_dict[n-1] = staircase_ways_dp(n-1)

        return memo_dict[n-1] + memo_dict[n-2]

def staircase_ways_variable_steps_rec(n, xs):
    if xs == None:
        return 0
    if n < 1:
        return 0
    elif n < min(xs):
        return 0
    else:
        sum = 0
        if (n in xs):
            sum += 1
        for x in xs:
            sum += staircase_ways_variable_steps_rec(n-x, xs)
        return sum

def staircase_ways_variable_steps_dp(n, xs):
    if xs == None:
        return 0
    if n < 1:
        return 0
    elif n < min(xs):
        return 0
    else:
        sum = 0
        if (n in xs):
            sum += 1
        for x in xs:
            if n-x not in memo_dict_var:
                memo_dict_var[n-x] = staircase_ways_variable_steps_dp(n-x, xs)
            sum += memo_dict_var[n-x]
        return sum


# print(staircase_ways_rec(35))
# print(staircase_ways_dp(7))
print([staircase_ways_variable_steps_dp(x, [1,3,5]) for x in range(20)])
# print(staircase_ways_variable_steps_rec(35, [1,3,5]))
# print(staircase_ways_variable_steps_dp(4, [1,3,5]))