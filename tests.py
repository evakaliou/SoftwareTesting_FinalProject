from input_generator import generate_input
from blockProbs_v1 import blocking_probabilities

def get_general_input():
    p1 = ["capacity", "int", [1.0], [10.0], 1]
    p2 = ["amount_of_routes", "int", [3.0], [8.0], 1]
    p3 = ["arrival_rates", "float", [0.0], [10.0], "amount_of_routes"]
    p4 = ["service_rates", "float", [1.0], [1.0], "amount_of_routes"]
    p5 = ["subset_amount_of_routes", "int", [2.0], ["amount_of_routes", "-", 1], 1]
    p6 = ["requirements_of_routes", "int", [1.0], ["capacity", "/", 2], "amount_of_routes"]
    return generate_input([p1, p2, p3, p4, p5, p6])

def get_same_rate_input():
    p1 = ["capacity", "int", [1.0], [10.0], 1]
    p2 = ["amount_of_routes", "int", [3.0], [8.0], 1]
    p3 = ["arrival_rate", "float", [0.0], [10.0], 1]
    p4 = ["arrival_rates", "float", ["arrival_rate"], ["arrival_rate"], "amount_of_routes"]
    p5 = ["service_rates", "float", [1.0], [1.0], "amount_of_routes"]
    p6 = ["subset_amount_of_routes", "int", [2.0], ["amount_of_routes", "-", 1], 1]
    p7 = ["requirements_of_routes", "int", [1.0], ["capacity", "/", 2], "amount_of_routes"]
    return generate_input([p1, p2, p3, p4, p5, p6,p7])


def metamorphic_test_small_vs_large_requirements():
    input = get_same_rate_input()
    sum_r = sum(input["arrival_rates"])
    C = input["capacity"]
    A = input["requirements_of_routes"]
    block_probs = blocking_probabilities(sum_r, C, A)
    # make sure that block_prob_i <= block_prob_j => A_i <= A_j
    # and block_prob >= block_prob_j => A_i >= A_j
    for i, p1 in enumerate(block_probs[:-1]):
        for j, p2 in enumerate(block_probs[i+1:]):
            if ( p1<=p2 and A[i]>A[j] ) or ( p1>=p2 and A[i]<A[j] ):
                print("problem")
                print(input)
                print(p1)
                print(p2)
                print(A[i])
                print(A[j])


metamorphic_test_small_vs_large_requirements()

