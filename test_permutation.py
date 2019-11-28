import math
from decimal import *
import random
import itertools

from input_generator_v2 import *
from blockProbs_v1 import *

input = generate_input()
bp0 = blocking_probabilities(sum(input['arrival_rates']), input['capacity'], input['requirement_of_route'])
print(input)

# only permute requirement of route
perm = list(itertools.permutations(input['requirement_of_route']))
bp_perm = list(itertools.permutations(bp0))
for i in range(len(perm)):
    assert [elem for elem in bp_perm[i]] == blocking_probabilities(sum(input['arrival_rates']), input['capacity'],[elem for elem in perm[i]]), str(
        [elem for elem in perm[i]])


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