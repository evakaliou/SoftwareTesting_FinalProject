import math
from decimal import *
import random

# for each route i, with requirement A[i]
# computes probability that the link 
# (with capacity C and total arrival to service rate ratio sum_r)
# has less than A[i] capacity left
def blocking_probabilities(sum_r,C,A):
# >>>>>>> CHANGE STARTS HERE <<<<<<<
    ss = steady_states(sum_r,C)
# >>>>>>> CHANGE ENDS HERE <<<<<<<
    result = []
    for i in range(len(A)):
        bp = 0
        for n in range(C-A[i]+1,C+1):
# >>>>>>> CHANGE STARTS HERE <<<<<<<
            bp += ss[n]
# >>>>>>> CHANGE ENDS HERE <<<<<<<
        result.append(bp)
    return result

# computes probability that link with capacity C 
# and arrival to service rate ratio r
# has n<=C of its capacity taken
def steady_state(r,C,n):
    result = 0
    nominator = pow(r,n)/math.factorial(n)
    denominator = pow(r,C)/math.factorial(C)
    for i in range(C):
        denominator+=(pow(r,i)/math.factorial(i))
    result = nominator/denominator
    return result

# >>>>>>> CHANGE STARTS HERE <<<<<<<
def steady_states(r,C):
    result = []
    for n in range(0,C+1):
        result.append(steady_state(r,C,n))
    return result
# >>>>>>> CHANGE ENDS HERE <<<<<<<
