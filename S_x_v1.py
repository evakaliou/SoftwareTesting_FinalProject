
class S_x:

    def __init__(self, A, X):
        self.A = A  # len(A)*2 matrix with resource requirements of each route
        self.X = X  # vector of size 2, capacity of each of two links

        self.current = [0]*len(A)  # "current" element; how many active routes of each type
        self.route = len(A) - 1 # route to check if one more can be added next
        self.rem1 = X[0]  # link 1 capacity remaining in *current* state
        self.rem2 = X[1]  # link 2 capacity remaining in *current* state
        self.res_per_route = [[0, 0] for x in range(len(A))]  # how much capacity taken by each type of route in *current*

    def get_next(self):
        if self.one_more_route_i_fits(self.route):
            self.add_one_more_route_i(self.route)
            return self.current
        else:
            self.remove_all_routes_of_type_i_or_greater(self.route)
            while self.route > 0:
                self.route -= 1
                if self.one_more_route_i_fits(self.route):
                    self.add_one_more_route_i(self.route)
                    return self.current
                else:
                    self.remove_all_routes_of_type_i(self.route)
            self.route = len(self.A)-1
            return self.current  # return "first" element which is all zeros

    def add_one_more_route_i(self, i):
        self.rem1 -= self.A[i][0]
        self.rem2 -= self.A[i][1]
        self.current[i] += 1
        self.res_per_route[i][0] += self.A[i][0]
        self.res_per_route[i][1] += self.A[i][1]

    def one_more_route_i_fits(self, i):
        return self.A[i][0] <= self.rem1 and self.A[i][1] <= self.rem2

    def remove_all_routes_of_type_i_or_greater(self, i):
        for j in range(i, len(self.A)):
            self.remove_all_routes_of_type_i(j)

    def remove_all_routes_of_type_i(self, i):
        self.rem1 += self.A[i][0] * self.current[i]
        self.rem2 += self.A[i][1] * self.current[i]
        self.res_per_route[i][0] = 0
        self.res_per_route[i][1] = 0
        self.current[i] = 0





