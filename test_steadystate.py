from blockProbs_v1 import steady_state as ss1
from blockProbs_v2 import steady_state as ss2

from blockProbs_v1 import blocking_probabilities as bp_v1
from blockProbs_v2 import blocking_probabilities as bp_v2

from blockProbs_v1 import G_c as gc1
from blockProbs_v2 import G_c as gc2

import unittest

#input = {'capacity': 9, 'amount_of_routes': 3, 'arrival_rates': [8.55733689499375, 0.05633419503270676, 9.353314995991157], 'service_rates': [1.0, 1.0, 1.0], 'subset_amount_of_routes': 2, 'requirements_of_routes': [2, 3, 1]}
input = {'capacity': 3, 'amount_of_routes': 4, 'arrival_rates': [5.831759720373354, 9.719823089899027, 1.479396216317913, 4.036158329394096], 'service_rates': [1.0, 1.0, 1.0, 1.0], 'subset_amount_of_routes': 3, 'requirements_of_routes': [1, 1, 1, 1]}
A = input['requirements_of_routes']
C = input['capacity']
class test_ss(unittest.TestCase):
    def ss(self):
        for i in range(len(A)):
            for n in range(C - A[i] + 1, C + 1):
                print(n)
                self.assertEqual(ss1(sum(input['arrival_rates']), C, n), ss2(sum(input['arrival_rates']), C, n))

    def bp(self):
        bp1 = bp_v1(sum(input['arrival_rates']), input['capacity'], input['requirements_of_routes'])
        bp2 = bp_v2(sum(input['arrival_rates']), input['capacity'], input['requirements_of_routes'])
        self.assertEqual( bp1 , bp2, str(input) + "bp1: " + str(bp1) + "bp2: " + str(bp2))

    def test_gc(self):
        for i in range(len(A)):
            for n in range(C - A[i] + 1, C + 1):
                self.assertEquals(gc1(sum(input['arrival_rates']), C), gc2(sum(input['arrival_rates']), C))

if __name__ == '__main__':
    unittest.main()