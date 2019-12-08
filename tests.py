import unittest

from input_generator import generate_input

from blockProbs.blockProbs_v1 import blocking_probabilities as bp_v1
from blockProbs.blockProbs_v2 import blocking_probabilities as bp_v2
from blockProbs.blockProbs_v3 import blocking_probabilities as bp_v3

from rateLoss.rateLoss_v1 import rate_of_loss as rl_v1
from rateLoss.rateLoss_v2 import rate_of_loss as rl_v2
from rateLoss.rateLoss_v3 import rate_of_loss as rl_v3


def get_same_rate_input():
    p1 = ["capacity", "int", [1.0], [10.0], 1]
    p2 = ["amount_of_routes", "int", [3.0], [8.0], 1]
    p3 = ["arrival_rate", "float", [0.0], [10.0], 1]
    p4 = ["arrival_rates", "float", ["arrival_rate"], ["arrival_rate"], "amount_of_routes"]
    p5 = ["service_rates", "float", [1.0], [1.0], "amount_of_routes"]
    p6 = ["subset_amount_of_routes", "int", [2.0], ["amount_of_routes", "-", 1], 1]
    p7 = ["requirements_of_routes", "int", [1.0], ["capacity", "/", 2], "amount_of_routes"]
    return generate_input([p1, p2, p3, p4, p5, p6, p7])


def get_general_input():
    p1 = ["capacity", "int", [1.0], [10.0], 1]
    p2 = ["amount_of_routes", "int", [3.0], [8.0], 1]
    p3 = ["arrival_rates", "float", [0.0], [10.0], "amount_of_routes"]
    p4 = ["service_rates", "float", [1.0], [1.0], "amount_of_routes"]
    p5 = ["subset_amount_of_routes", "int", [2.0], ["amount_of_routes", "-", 1], 1]
    p6 = ["requirements_of_routes", "int", [1.0], ["capacity", "/", 2], "amount_of_routes"]
    return generate_input([p1, p2, p3, p4, p5, p6])


class TestOneEdge(unittest.TestCase):

    def test_blockProbs_small_vs_large_requirements(self):
        input = get_same_rate_input()
        sum_r = sum(input["arrival_rates"])
        C = input["capacity"]
        A = input["requirements_of_routes"]
        block_probs = bp_v1(sum_r, C, A)
        # make sure that block_prob_i <= block_prob_j => A_i <= A_j
        # and block_prob >= block_prob_j => A_i >= A_j
        for i, p1 in enumerate(block_probs[:-1]):
            for j in range(i+1, len(block_probs)):
                p2 = block_probs[j]
            # mystery: changing the inner for loop from below to above resulted in correct test runs
            # for j, p2 in enumerate(block_probs[i+1:]):
                if p1 < p2:
                    message = "Route "+str(i)+" has smaller block prob than route "+str(j)+" "
                    message += "("+str(p1)+" and "+str(p2)+" respectively),"
                    message += "but greater resource requirements "
                    message += "(" + str(A[i]) + " and " + str(A[j]) + " respectively),"
                    value = bool(A[i] <= A[j])
                    self.assertTrue(value, str(message))
                elif p1 > p2:
                    message = "Route " + str(i) + " has greater block prob than route " + str(j) + " "
                    message += "(" + str(p1) + " and " + str(p2) + " respectively),"
                    message += "but smaller resource requirements "
                    message += "(" + str(A[i]) + " and " + str(A[j]) + " respectively),"
                    value = bool(A[i] >= A[j])
                    self.assertTrue(value, str(message))

    def test_simple_cases(self):
        p1 = ["capacity", "int", [1.0], [10.0], 1]
        p2 = ["amount_of_routes", "int", [3.0], [8.0], 1]
        p3 = ["arrival_rates", "float", [0.0], [0.0], "amount_of_routes"]
        p4 = ["service_rates", "float", [1.0], [1.0], "amount_of_routes"]
        p5 = ["subset_amount_of_routes", "int", [2.0], ["amount_of_routes", "-", 1], 1]
        p6 = ["requirements_of_routes", "int", [1.0], ["capacity", "/", 2], "amount_of_routes"]

        input = generate_input([p1, p2, p3, p4, p5, p6])

        bp = bp_v1(sum(input['arrival_rates']), input['capacity'], input['requirements_of_routes'])

        for i in range(input['amount_of_routes']):
            assert (not input['arrival_rates'][i] == 0) or bp[i] == 0, "arrival rate is " + str(
                input['arrival_rates'][i]) + "blocking prob is " + str(bp[i])
            assert (not input['requirements_of_routes'][i] == 0) or bp[i] == 0, "requirement is " + str(
                input['requirements_of_routes'][i]) + "blocking prob is " + str(bp[i])

    def test_permutations_bp(self):
        p1 = ["capacity", "int", [1.0], [10.0], 1]
        p2 = ["amount_of_routes", "int", [3.0], [8.0], 1]
        p3 = ["arrival_rates", "float", [0.0], [10.0], "amount_of_routes"]
        p4 = ["service_rates", "float", [1.0], [1.0], "amount_of_routes"]
        p5 = ["subset_amount_of_routes", "int", [2.0], ["amount_of_routes", "-", 1], 1]
        p6 = ["requirements_of_routes", "int", [1.0], ["capacity", "/", 2], "amount_of_routes"]

        input = generate_input([p1, p2, p3, p4, p5, p6])
        bp1 = bp_v1(sum(input['arrival_rates']), input['capacity'], input['requirements_of_routes'])
        bp2 = bp_v2(sum(input['arrival_rates']), input['capacity'], input['requirements_of_routes'])
        bp3 = bp_v3(sum(input['arrival_rates']), input['capacity'], input['requirements_of_routes'])
        #assert bp1 == bp2, str(input) + "bp1: " + str(bp1) + "bp2: " + str(bp2)
        assert bp1 == bp3, str(input) + "bp1: " + str(bp1) + "bp3: " + str(bp3)

    def test_permutations_lossRate(self):
        p1 = ["capacity", "int", [1.0], [10.0], 1]
        p2 = ["amount_of_routes", "int", [3.0], [8.0], 1]
        p3 = ["arrival_rates", "float", [0.0], [10.0], "amount_of_routes"]
        p4 = ["service_rates", "float", [1.0], [1.0], "amount_of_routes"]
        p5 = ["subset_amount_of_routes", "int", [2.0], ["amount_of_routes", "-", 1], 1]
        p6 = ["requirements_of_routes", "int", [1.0], ["capacity", "/", 2], "amount_of_routes"]


        input = generate_input([p1, p2, p3, p4, p5, p6])

        bp1 = bp_v1(sum(input['arrival_rates']), input['capacity'], input['requirements_of_routes'])
        bp2 = bp_v2(sum(input['arrival_rates']), input['capacity'], input['requirements_of_routes'])
        bp3 = bp_v3(sum(input['arrival_rates']), input['capacity'], input['requirements_of_routes'])

        lossRate1 = rl_v1(bp1, input["arrival_rates"], input["service_rates"])
        lossRate2 = rl_v2(bp1, input["arrival_rates"], input["service_rates"])
        lossRate3 = rl_v3(bp3, input["arrival_rates"], input["service_rates"])

        assert lossRate1 == lossRate3, str(input) + "lossRate1: " + str(lossRate1) + ", lossRate3: " + str(lossRate3)
        assert lossRate1 == lossRate2, str(input) + "lossRate1: " + str(lossRate1) + ", lossRate2: " + str(lossRate2)

    def test_rateLoss_monotonicity(self):
        input = get_general_input()
        subset_amount_of_routes = input["subset_amount_of_routes"]
        sum_r = sum(input["arrival_rates"])
        C = input["capacity"]
        A = input["requirements_of_routes"]
        arrRates = input["arrival_rates"]
        serRates = input["service_rates"]
        block_prob = bp_v1(sum_r, C, A)
        lossRate = rl_v1(block_prob, arrRates, serRates)
        for i in range(subset_amount_of_routes):
            A_new = A[0:i]
            A_new += A[i + 1:]
            arrRates_new = arrRates[0:i]
            arrRates_new += arrRates[i + 1:]
            serRates_new = serRates[0:i]
            serRates_new += serRates[i + 1:]

            block_prob_new = bp_v1(sum(arrRates_new), C, A_new)
            lossRate_new = rl_v1(block_prob_new, arrRates_new, serRates_new)

            message = "By removing route "+ str(i)+ " the rate of loss becomes "+ str(lossRate_new)
            message += ". Its original value was "+str(lossRate)
            self.assertTrue(bool(lossRate_new <= lossRate), str(message))


if __name__ == '__main__':
    unittest.main()




