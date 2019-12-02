import math
from decimal import *
import random

from input_generator_v1 import *
from blockProbs_v1 import *
from input_generator import generate_input

p1 = ["capacity", "int", [1.0], [10.0], 1]
p2 = ["amount_of_routes", "int", [3.0], [8.0], 1]
p3 = ["arrival_rates", "float", [0.0], [0.0], "amount_of_routes"]
p4 = ["service_rates", "float", [1.0], [1.0], "amount_of_routes"]
p5 = ["subset_amount_of_routes", "int", [2.0], ["amount_of_routes", "-", 1], 1]
p6 = ["requirements_of_routes", "int", [1.0], ["capacity", "/", 2], "amount_of_routes"]

#input = input()

input = generate_input([p1, p2, p3, p4, p5, p6])

# A = []  # will hold the amount of resources each route needs
# for i in range(input['amount_of_routes']):
#     A.append(random.randint(1, math.ceil(input['capacity'] / 2)))
bp = blocking_probabilities(sum(input['arrival_rates']), input['capacity'], input['requirements_of_routes'])
print(input)
print(bp)
for i in range(input['amount_of_routes']):
    assert (not input['arrival_rates'][i] == 0) or bp[i] == 0, "arrival rate is " + str(input['arrival_rates'][i]) + "blocking prob is " + str(bp[i])
    assert (not input['requirements_of_routes'][i] == 0) or bp[i] == 0, "requirement is " + str(input['requirements_of_routes'][i]) + "blocking prob is " + str(bp[i])