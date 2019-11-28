from input_generator import generate_input
from blockProbs_v1 import blocking_probabilities
from input_generator import get_general_input
from input_generator import get_same_rate_input
import unittest


class TestOneEdge(unittest.TestCase):

    def test_metamorphic1_small_vs_large_requirements(self):
        input = get_same_rate_input()
        sum_r = sum(input["arrival_rates"])
        C = input["capacity"]
        A = input["requirements_of_routes"]
        block_probs = blocking_probabilities(sum_r, C, A)
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


if __name__ == '__main__':
    unittest.main()




