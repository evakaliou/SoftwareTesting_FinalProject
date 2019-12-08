import math
from decimal import *
import random

# computes the sum, over all routes,
# of the arrival to service rate ration, times the blocking probability
def rate_of_loss(block_prob,arrRates,serRates):
    result = 0
    for i in range(len(block_prob)):
# >>>>>>> CHANGE STARTS HERE <<<<<<<
        result += arrRates[i]*block_prob[i]/serRates[i]
# >>>>>>> CHANGE ENDS HERE <<<<<<<
    return result
