import math
from decimal import *
import random
import itertools

from input_generator_v2 import *
from blockProbs_v1 import *

from rateLoss_v1 import rate_of_loss

from input_generator import get_general_input

input = generate_input()
bp0 = blocking_probabilities(sum(input['arrival_rates']), input['capacity'], input['requirement_of_route'])
print(input)

# only permute requirement of route
perm = list(itertools.permutations(input['requirement_of_route']))
bp_perm = list(itertools.permutations(bp0))
for i in range(len(perm)):
    assert [elem for elem in bp_perm[i]] == blocking_probabilities(sum(input['arrival_rates']), input['capacity'],[elem for elem in perm[i]]), str(
        [elem for elem in perm[i]])

input2 = get_general_input()

bp2 = blocking_probabilities(sum(input2['arrival_rates']), input2['capacity'], input2['requirements_of_routes'])
perm2 = list(itertools.permutations(input2['arrival_rates']))
bp2_perm = list(itertools.permutations(bp2))
ser_perm = list(itertools.permutations(input2["service_rates"]))

loss_rate0 = rate_of_loss(bp2, input2["arrival_rates"], input2["service_rates"])

print(str(input2))

print("LR1: " + str((rate_of_loss([elem for elem in bp2_perm[1]], [elem for elem in perm2[1]], [elem for elem in ser_perm[1]]))))
print("LR2L " + str((loss_rate0)))

assert [elem for elem in bp_perm[0]]==bp0
for i in range(len(bp_perm)):
    rl1 = rate_of_loss([elem for elem in bp2_perm[i]], [elem for elem in perm2[i]], [elem for elem in ser_perm[i]])
    assert rl1 ==loss_rate0, str(rl1) + "XXX" + str(loss_rate0)
    #lossRate1 = rate_of_loss(bp0, input2["arrival_rates"], input2["service_rates"])

# if input['amount_of_routes'] == 3:
#     print(input)
#     # only permute requirement of route
#     perm = list(itertools.permutations(input['requirement_of_route']))
#     bp_perm = list(itertools.permutations(bp0))
#     for i in range(len(perm)):
#         assert [elem for elem in bp_perm[i]] == blocking_probabilities(sum(input['arrival_rates']), input['capacity'], [elem for elem in perm[i]]), str([elem for elem in perm[i]])
#
# else:
#     # since when amount_of_routes==3 is always correct,
#     #  only need to check different last ones
#     print(input)
#     for i in range(input['amount_of_routes']):
#         perm = input['requirement_of_route'][:i] + input['requirement_of_route'][i+1:] + [input['requirement_of_route'][i]]
#         bp_perm = bp0[:i] + bp0[i+1:] + [bp0[i]]
#         assert bp_perm == blocking_probabilities(sum(input['arrival_rates']), input['capacity'], perm), str(perm)