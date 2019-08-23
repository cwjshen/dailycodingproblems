# This problem was asked by Facebook.

# A builder is looking to build a row of N houses that can be of K different colors.
# He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, 
# return the minimum cost which achieves this goal.

# Leetcode 265 - Paint House 2
# =============INCOMPLETE==========

# N = 1,2,3
# K = a,b

# NxK = 
# [[1a, 2a, 3a],
#  [1b, 2b, 3b]]

# Get the index of the color that corresponds to the minimum cost color for a given house
def get_min_cost(house_costs):
    curr_min = None
    min_index = 0
    for index, cost in enumerate(house_costs):
        if curr_min == None or cost < curr_min:
            curr_min = cost
            min_index = index
    return (min_index, curr_min)

def min_total_cost(cost_matrix):
    # Base case, if there is only a single house, return minimum cost of that house
    if len(cost_matrix) == 1:
        return get_min_cost(cost_matrix[0])

    total_cost = 0
    # Iterate through each house
    for index, house in enumerate(cost_matrix):
        # Get minimum cost of the current house
        curr_house_min = get_min_cost(house)[1]
        total_cost += curr_house_min
    return total_cost

def main():
    houses = [i for i in range(1, 5)]
    colors = [j for j in range(11, 15)]
    cost_matrix = []

    for house in houses:
        house_costs = []
        for color in colors:
            house_costs.append(house * color)
        cost_matrix.append(house_costs)
    print(cost_matrix)

    for houses in cost_matrix:
        print(get_min_cost(houses))

    print(min_total_cost(cost_matrix))
main()