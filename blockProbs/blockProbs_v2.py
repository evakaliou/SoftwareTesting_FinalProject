import math
from decimal import *
import random

# >>>>>>> CHANGE STARTS HERE <<<<<<<
def G_c(sum_r,C):
    result = sum_r
    nominator = 1
    denominator = 1
    for n in range(1, C+1):
        nominator = nominator * sum_r
        denominator = denominator * n
        result += nominator/denominator
    return result
# >>>>>>> CHANGE ENDS HERE <<<<<<<


# for each route i, with requirement A[i]
# computes probability that the link
# (with capacity C and total arrival to service rate ratio sum_r)
# has less than A[i] capacity left
def blocking_probabilities(sum_r, C, A):
    result = []
    for i in range(len(A)):
        # print("Probability that route "+str(i)+" is blocked = ")
        bp = 0
        for n in range(C-A[i]+1, C+1):
            # print("probability that there are "+str(n)+" active routes")
            bp += steady_state(sum_r, C, n)
        result.append(bp)
    return result


# computes probability that link with capacity C 
# and arrival to service rate ratio r
# has n<=C of its capacity taken
def steady_state(sum_r, C, n):
    result = 0
# >>>>>>> CHANGE STARTS HERE <<<<<<<
    nominator = pow(sum_r, n)/math.factorial(n)
    result = nominator/ G_c(sum_r, C)
# >>>>>>> CHANGE ENDS HERE <<<<<<<
    return result
