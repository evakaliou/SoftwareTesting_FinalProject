import math
from decimal import *
import random


# for each route i, with requirement A[i]
# computes probability that the link 
# (with capacity C and total arrival to service rate ratio sum_r)
# has less than A[i] capacity left
def blocking_probabilities(sum_r, C, A):
    result = []
    for i in range(len(A)):
        bp = 0
        for n in range(C-A[i]+1, C+1):
            bp += steady_state(sum_r, C, n)
        result.append(bp)
    return result


# computes probability that link with capacity C 
# and arrival to service rate ratio r
# has n<=C of its capacity taken
def steady_state(r, C, n):
    nominator = pow(r, n) / math.factorial(n)
    denominator = pow(r, C) / math.factorial(C)
    for i in range(C):
        denominator += pow(r, i) / math.factorial(i)
    ss_result = nominator/denominator
    return ss_result

def G_c(r, C):
    denominator = pow(r, C) / math.factorial(C)
    for i in range(C):
        denominator += pow(r, i) / math.factorial(i)

    return denominator
