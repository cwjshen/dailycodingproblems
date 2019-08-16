# This problem was asked by Google.
# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
# Hint: The basic equation of a circle is x2 + y2 = r2.

import random
import math

# Function to 
def sample_pi(num_samples):
    # If the area of a circle is pi*r^2, we can inscribe a quarter of a circle with radius of 1 within a unit square
    # Thus exactly (pi*r^2 / 4) where r = 1 --> pi/4 area of circle is within the unit square.
    # tl;dr out of a square area of 1, pi/4 area belongs to the circle
    area = 1

    random_rs = []
    # We sample a bunch of X's and Y's between 0 and 1
    for i in range(num_samples):
        random_x = random.random()
        random_y = random.random()

        # You calculate the r value for random sample x and y
        # Over a large enough number of samples, the ratio of number of r's that have a value of less than 1 to the total number of r's
        #   should be about pi/4

        random_rs.append(random_x*random_x + random_y*random_y)

    counter = 0
    for r in random_rs:
        if r < 1:
            counter += 1
    return counter / len(random_rs) * 4

print(sample_pi(100000))
    