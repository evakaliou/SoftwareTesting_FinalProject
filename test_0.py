import math
from decimal import *
import random

from input_generator_v1 import *
from blockProbs_v1 import *

input = input()
A = []  # will hold the amount of resources each route needs
for i in range(input['amount_of_routes']):
    A.append(random.randint(1, math.ceil(input['capacity'] / 2)))
bp = blocking_probabilities(sum(input['arrival_rates']), input['capacity'], input['requirement_of_route'])
print(input)
print(bp)
for i in range(input['amount_of_routes']):
    assert (not input['arrival_rates'][i] == 0) or bp[i] == 0, "arrival rate is " + str(input['arrival_rates'][i]) + "blocking prob is " + str(bp[i])
    assert (not input['requirement_of_route'][i] == 0) or bp[i] == 0, "requirement is " + str(input['requirement_of_route'][i]) + "blocking prob is " + str(bp[i])