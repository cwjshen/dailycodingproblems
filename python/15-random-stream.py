# This problem was asked by Facebook.
# Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

import random
import math

def pick_random(prev_element, next_element, size):
    current_prob = 1/size
    roll = random.random()
    if roll < current_prob:
        return next_element
    return prev_element

def mock_stream(stream_size):
    current_size = 1
    # Our mock stream of elements will just be i from 0 -> MAX_INT 
    stream_element = 0
    prev = None
    solution = -1
    while stream_element < stream_size:
        solution = pick_random(prev, stream_element, current_size)
        stream_element += 1
        current_size += 1
        prev = solution
    return solution

def main():
    # We want to see over many runs, that the numbers are indeed picked approximately uniformly
    
    # We will use a dict to track how many times a number is picked by our picker method
    picked_dict = {}
    iterations = 100
    stream_size = 50

    for i in range(iterations):
        picked = mock_stream(stream_size)
        if picked not in picked_dict:
            picked_dict[picked] = 1
        else:
            picked_dict[picked] += 1

    # We'll look at standard deviation to gauge how close we are to being uniform
    # For a uniform distribution, we expect the count for each random variable to be the same

    expected_count = iterations / stream_size
    running_sum_of_sq_err = 0
    for key in picked_dict:
        running_sum_of_sq_err += (picked_dict[key] - expected_count)**2
    std_dev = math.sqrt(running_sum_of_sq_err / stream_size)
    error_percent = std_dev / expected_count * 100
    print(picked_dict)
    print('Expected count: ', expected_count)
    # print('Counts: ', picked_dict)
    print('Standard Deviation: ', std_dev)
    print('Average error percentage: ', error_percent, '%')
main()