import math
from decimal import *
import random

# >>>>>>> CHANGE STARTS HERE <<<<<<<
def G_c(sum_r,C):
    result = sum_r
    nominator = 1
    denominator = 1
    for n in range(1,C+1):
        nominator = nominator * sum_r
        denominator = denominator * n
        result += nominator/denominator
    return result
# >>>>>>> CHANGE ENDS HERE <<<<<<<

# computes the sum, over all routes,
# of the arrival to service rate ration, times the blocking probability
def rate_of_loss(block_prob,arrRates,serRates):
    result = 0
    for i in range(len(block_prob)):
        result += (arrRates[i]/serRates[i])*block_prob[i]
    return result

# computes probability that link with capacity C 
# and arrival to service rate ratio r
# has n<=C of its capacity taken
def steady_state(r,C,n):
    result = 0
# >>>>>>> CHANGE STARTS HERE <<<<<<<
    nominator = pow(r,n)/math.factorial(n)
    result = nominator/ G_c(r,C)
# >>>>>>> CHANGE ENDS HERE <<<<<<<
    return result
