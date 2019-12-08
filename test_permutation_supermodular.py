from supermodularCheck_v1 import supermod_check

from blockProbs_v1 import blocking_probabilities
import itertools

input = {'capacity': 8, 'amount_of_routes': 6, 'arrival_rates': [8.072139958401321, 5.141731611404376, 7.739513655374174, 7.12979829481788, 0.2851654237091783, 4.077820349486901],
         'service_rates': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0], 'subset_amount_of_routes': 4, 'requirements_of_routes': [4, 4, 3, 1, 4, 1]}
#C: capacity
#A: requirements_of_routes
#supermod_check(C, A, arrRates, serRates, subsetAmountOfRoutes)
reqirements_of_routes = input['requirements_of_routes']
arrival_rates = input['arrival_rates']

list_of_tuple = []
for i in range(len(reqirements_of_routes)):
    list_of_tuple.append((reqirements_of_routes[i], arrival_rates[i]))

#print(str(list_of_tuple))
#print(str([elem[0] for elem in list_of_tuple]))
list_perm = list(itertools.permutations(list_of_tuple))
#print ([elem[0] for elem in list_perm[0]])

for i in range(len(list_perm)):
    requirements_of_routes_temp = [elem[0] for elem in list_perm[i]]
    arrival_rates_temp = [elem[1] for elem in list_perm[i]]
    assert supermod_check(input['capacity'], input['requirements_of_routes'], arrival_rates, input['service_rates'], input['subset_amount_of_routes']) == supermod_check(input['capacity'], requirements_of_routes_temp, arrival_rates_temp,
                          input['service_rates'], input['subset_amount_of_routes']), str(requirements_of_routes_temp) + str(arrival_rates_temp)

# A_perm = list(itertools.permutations(reqirements_of_routes))
# arrRates_perm = list(itertools.permutations(arrival_rates))
#
# blocking_probabilities(sum(input['arrival_rates']), input['capacity'], input['requirements_of_routes'])
#
# assert supermod_check(input['capacity'], input['requirements_of_routes'], arrival_rates, input['service_rates'], input['subset_amount_of_routes'])
#
# for i in range(len(A_perm)):
#     assert supermod_check(input['capacity'], [elem for elem in A_perm[i]], [elem for elem in arrRates_perm[i]], input['service_rates'], input['subset_amount_of_routes']), "arrival rate: " + str(A_perm[i]) + "\n" + str(arrRates_perm[i])
