import random
import sys
import math


# parameter names are unique
# if a parameter bound depends on another parameter, it has to be a previous parameter with amount = 1
# no bound starts/ends in a numerical operator
# no bound has two operators as a substring
# no bound has /0 as a substring
# no bound has two consecutive numbers, parameters, or parameter-number pair as a substring
def check_input():
    # makes sure that input is ok
    print("Disclaimer: We are not checking the input yet so we don't take responsibility for crappy inputs ")


def quantify_bound(bound, params):

    # INPUT
    # bound: non-null array. if non-empty, form is
    #  [ number|param_name, num_oper, number|param_name, ... , number|param_name ]
    #  (note: full constraints given in def check_input)
    # params: dictionary with (param_name, value) pairs
    # OUTPUT
    # result of expression

    b_result = [c for c in bound]
    operators = ["*", "/", "+", "-"]
    for op in operators:
        try:
            i = b_result.index(op)
        except ValueError:
            i = -1
        while i != -1:
            left = b_result[i-1]
            if b_result[i-1] in params:
                left = params[b_result[i-1]]
            right = b_result[i + 1]
            if b_result[i + 1] in params:
                right = params[b_result[i + 1]]
            left = float(left)
            right = float(right)
            if op == "*":
                b_result[i-1] = left*right
            elif op == "/":
                b_result[i - 1] = left/right
            elif op == "+":
                b_result[i - 1] = left+right
            else:
                b_result[i - 1] = left-right
            del b_result[i]
            del b_result[i]
            try:
                i = b_result.index(op)
            except ValueError:
                i = -1
    if len(b_result) != 1:
        sys.exit('def quantify bound : Outcome is not a single number')
    if b_result[0] in params:
        b_result[0] = float(params[b_result[0]])
    return b_result[0]

def generate_input(parameters):

    check_input()
    result = dict()

    for p in parameters:
        name_of_par = p[0]
        type_of_par = p[1]
        lower = quantify_bound(p[2], result)
        upper = quantify_bound(p[3], result)
        if type_of_par == "int":
            lower = int(math.ceil(lower))
            upper = int(math.floor(upper))
        amount = p[4]
        if lower > upper:
            print('lower and upper bound incompatibility for parameter '+name_of_par+". Trying again.")
            return generate_input(parameters)
        if amount in result:
            amount = result[amount]
        if amount == 1:
            if type_of_par == "int":
                result[name_of_par] = random.randint(lower, upper)
            else:
                result[name_of_par] = random.uniform(lower, upper)
        else:
            if type_of_par == "int":
                result[name_of_par] = [random.randint(lower, upper) for i in range(amount)]
            else:
                result[name_of_par] = [random.uniform(lower, upper) for i in range(amount)]

    return result
