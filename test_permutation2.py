import itertools
from blockProbs_v1 import blocking_probabilities
from rateLoss_v1 import rate_of_loss
from input_generator import generate_input
import unittest

class permutation(unittest.TestCase):
    def block_prob(self):
        p1 = ["capacity", "int", [1.0], [10.0], 1]
        p2 = ["amount_of_routes", "int", [3.0], [8.0], 1]
        p3 = ["arrival_rates", "float", [0.0], [10.0], "amount_of_routes"]
        p4 = ["service_rates", "float", [1.0], [1.0], "amount_of_routes"]
        p5 = ["subset_amount_of_routes", "int", [2.0], ["amount_of_routes", "-", 1], 1]
        p6 = ["requirements_of_routes", "int", [1.0], ["capacity", "/", 2], "amount_of_routes"]

        input = generate_input([p1, p2, p3, p4, p5, p6])

        bp0 = blocking_probabilities(sum(input['arrival_rates']), input['capacity'], input['requirements_of_routes'])

        list_of_tuples = []
        for i in range(len(input['requirements_of_routes'])):
            list_of_tuples.append((input['requirements_of_routes'][i], bp0[i]))

        list_perm = list(itertools.permutations(list_of_tuples))

        # r_r = [elem[0] for elem in list_perm[0]]
        # assert r_r == input['requirements_of_routes'], "r_r: " + str(r_r) + "\nr_r0: " + str(input['requirements_of_routes'])

        for i in range(len(list_perm)):
            r_r = [elem[0] for elem in list_perm[i]]
            bp_temp = blocking_probabilities(sum(input['arrival_rates']), input['capacity'], r_r)
            bp = [elem[1] for elem in list_perm[i]]
            self.assertEqual(bp, bp_temp, "BP: "+str(bp)+"new BP"+str(bp_temp))

    def test_loss_rate(self):
        p1 = ["capacity", "int", [1.0], [10.0], 1]
        p2 = ["amount_of_routes", "int", [3.0], [8.0], 1]
        p3 = ["arrival_rates", "float", [0.0], [10.0], "amount_of_routes"]
        p4 = ["service_rates", "float", [1.0], [1.0], "amount_of_routes"]
        p5 = ["subset_amount_of_routes", "int", [2.0], ["amount_of_routes", "-", 1], 1]
        p6 = ["requirements_of_routes", "int", [1.0], ["capacity", "/", 2], "amount_of_routes"]

        input = generate_input([p1, p2, p3, p4, p5, p6])
        print(str(input))
        bp0 = blocking_probabilities(sum(input['arrival_rates']), input['capacity'], input['requirements_of_routes'])
        loss_rate0 = rate_of_loss(bp0, input['arrival_rates'], input['service_rates'])

        list_of_tuples = []
        for i in range(len(bp0)):
            list_of_tuples.append((bp0[i], input['arrival_rates'][i], input['service_rates'][i]))

        list_perm = list(itertools.permutations(list_of_tuples))
        for i in range(len(list_perm)):
            bp = [elem[0] for elem in list_perm[i]]
            arr_rates = [elem[1] for elem in list_perm[i]]
            ser_rates = [elem[2] for elem in list_perm[i]]
            loss_rate = rate_of_loss(bp, arr_rates, ser_rates)
            self.assertEqual(loss_rate0, loss_rate, "lossrate0: " + str(loss_rate0) + "\nlossrate: " + str(loss_rate))
            # try:
            #     self.assertEqual(loss_rate0, loss_rate, "lossrate0: " + str(loss_rate0) + "\nlossrate: " + str(loss_rate))
            # except AssertionError as e:
            #     print(e)

if __name__ == '__main__':
    unittest.main()