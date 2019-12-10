import unittest

from input_generator import generate_input
from S_x_v1 import S_x


def get_general_input():
    p0 = ["amount_of_routes", "int", [3.0], [8.0], 1]
    p1 = ["X1", "int", [2.0], [10.0], 1]
    p2 = ["X2", "int", [2.0], [10.0], 1]
    p3 = ["A1", "int", [1.0], ["X1","/",2], "amount_of_routes"]
    p4 = ["A2", "int", [1.0], ["X2","/",2], "amount_of_routes"]
    temp_result = generate_input([p0, p1, p2, p3, p4])
    result = dict()
    result["X"] = [temp_result["X1"], temp_result["X2"]]
    result["A"] = []
    for i in range(temp_result["amount_of_routes"]):
        result["A"].append([temp_result["A1"][i], temp_result["A2"][i]])
    return result


def get_more_than_half_input():
    result = get_general_input()
    # randomly modify first three routes s.t.
    # first has requirement > X1/2
    # second has requirement > X2/2
    # third has requirement > X1/2 and >X2/2
    p0 = ["link1", "int", [result["X"][0], "/", 2, "+", 1], [result["X"][0]], 2]
    p1 = ["link2", "int", [result["X"][1], "/", 2, "+", 1], [result["X"][1]], 2]
    sub_result = generate_input([p0, p1])
    result["A"][0][0] = sub_result["link1"][0]
    result["A"][1][1] = sub_result["link2"][0]
    result["A"][2][0] = sub_result["link1"][1]
    result["A"][2][1] = sub_result["link2"][1]
    return result


class TestSx(unittest.TestCase):

    # metamorphic test1:
    # if a route r requires more than half of the capacity of some link,
    # getNext should never return a state where there are more than 1 routes r
    def test_more_than_half(self):
        input = get_more_than_half_input()
        A = input["A"]
        X = input["X"]
        testSet = S_x(A , X)
        next = testSet.get_next()
        print(next)
        while not all([v == 0 for v in next]) :
            # check that amount of routes 0, 1, 2 are at most 1
            value = bool(next[0] <= 1)
            self.assertTrue(value, str(input))
            value = bool(next[1] <= 1)
            self.assertTrue(value, str(input))
            value = bool(next[2] <= 1)
            self.assertTrue(value, str(input))
            next = testSet.get_next()
            print(next)

    def test_does_not_exceed(self):
        input = get_general_input()
        A = input["A"]
        X = input["X"]
        testSet = S_x(A, X)
        next = testSet.get_next()
        print(next)
        while not all([v == 0 for v in next]):
            # check that the sum of requirements of each route for a link
            # does not exceed the capacity of that link
            value = bool( sum([next[i]*A[i][0] for i in range(len(A))]) <= X[0])
            self.assertTrue(value, str(input))
            value = bool( sum([next[i]*A[i][1] for i in range(len(A))]) <= X[1])
            next = testSet.get_next()
            print(next)