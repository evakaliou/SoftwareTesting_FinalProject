import unittest

from input_generator import generate_input

from S_x_v1 import S_x

class test_S(unittest.TestCase):
    def test_get_next(self):
        #s = S_x([[5, 6], [20, 20]], [20, 20])
        p1 = ["capacity1", "int", [1.0], [10.0], 1] # capacity of link 1
        p2 = ["capacity2", "int", [1.0], [10.0], 1] # capacity of link 2
        p3 = ["amount_of_routes", "int", [3.0], [8.0], 1] # amount of routes
        p4 = ["requirements_of_routes1", "int", [1.0], ["capacity1", "/", 2], "amount_of_routes"]
        p5 = ["requirements_of_routes2", "int", [1.0], ["capacity2", "/", 2], "amount_of_routes"]
        input = generate_input([p1, p2, p3, p4, p5])
        print(str(input))

        A = [[input["requirements_of_routes1"][i],input["requirements_of_routes2"][i]] for i in range(input["amount_of_routes"])]
        print(str(A))
        s = S_x(A, [input["capacity1"], input["capacity2"]])

        current = s.get_next()
        while (not all(i ==0 for i in current)):
            print(current)
            current = s.get_next()
        #print(str(s.current)+"#"+str(s.route)+"#"+str(s.rem1)+"#"+str(s.rem2)+"#"+str(s.res_per_route))
        # print(str(s.get_next()))
        # print(str(s.get_next()))
        # print(str(s.get_next()))
        # print(str(s.get_next()))
        # print(str(s.get_next()))
        # print(str(s.get_next()))
        # print(str(s.get_next()))
        # print(str(s.get_next()))
        # print(str(s.get_next()))
        #self.assertEqual(s.get_next(), [6,0], s.get_next())

if __name__ == '__main__':
    unittest.main()