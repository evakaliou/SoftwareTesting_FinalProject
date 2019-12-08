from blockProbs_v1 import blocking_probabilities as bp_v1
from blockProbs_v2 import blocking_probabilities as bp_v2
from blockProbs_v3 import blocking_probabilities as bp_v3

from rateLoss_v1 import rate_of_loss as rl_v1
from rateLoss_v2 import rate_of_loss as rl_v2
from rateLoss_v3 import rate_of_loss as rl_v3

from input_generator import generate_input

p1 = ["capacity", "int", [1.0], [10.0], 1]
p2 = ["amount_of_routes", "int", [3.0], [8.0], 1]
p3 = ["arrival_rates", "float", [0.0], [10.0], "amount_of_routes"]
p4 = ["service_rates", "float", [1.0], [1.0], "amount_of_routes"]
p5 = ["subset_amount_of_routes", "int", [2.0], ["amount_of_routes", "-", 1], 1]
p6 = ["requirements_of_routes", "int", [1.0], ["capacity", "/", 2], "amount_of_routes"]


#input = get_general_input()
input = generate_input([p1, p2, p3, p4, p5, p6])
bp1 = bp_v1(sum(input['arrival_rates']), input['capacity'], input['requirements_of_routes'])
bp2 = bp_v2(sum(input['arrival_rates']), input['capacity'], input['requirements_of_routes'])
bp3 = bp_v3(sum(input['arrival_rates']), input['capacity'], input['requirements_of_routes'])
assert bp1 == bp2, str(input) + "bp1: " + str(bp1) + "bp2: " + str(bp2)
assert bp1 == bp3, str(input) + "bp1: " + str(bp1) + "bp3: " + str(bp3)

lossRate1 = rl_v1(bp1, input["arrival_rates"], input["service_rates"])
lossRate2 = rl_v2(bp2, input["arrival_rates"], input["service_rates"])
lossRate3 = rl_v3(bp3, input["arrival_rates"], input["service_rates"])

assert lossRate1 == lossRate3, str(input) + "lossRate1: " + str(lossRate1) + ", lossRate3: " + str(lossRate3)
assert lossRate1 == lossRate2, str(input) + "lossRate1: " + str(lossRate1) + ", lossRate2: " + str(lossRate2)