import math
from decimal import *
import random

# for each route i, with requirement A[i]
# computes probability that the link 
# (with capacity C and total arrival to service rate ratio sum_r)
# has less than A[i] capacity left
def blocking_probabilities(sum_r,C,A):
    result = []
    for i in range(len(A)):
        bp = 0
        for n in range(C-A[i]+1,C+1):
            bp += steady_state(sum_r,C,n)
        result.append(bp)
    return result

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
    nominator = pow(r,n)/math.factorial(n)
    denominator = pow(r,C)/math.factorial(C)
    for i in range(C):
        denominator+=(pow(r,i)/math.factorial(i))
    result = nominator/denominator
    return result


monotonicityFlag = False
blockingFlag = False
supermodFlag = False

while not monotonicityFlag and not blockingFlag and not supermodFlag:  
    C = random.randint(1,10) #required: minimum value of 1
    print("Edge Capacity is")
    print(C)
    amountOfRoutes = random.randint(3,8) #required: minimum value of 3
    print("Amount of routes")
    print(amountOfRoutes)
    A=[] #will hold the amount of resources each route needs
    arrRates=[] #will hold the arrival rate of each route
    serRates=[] #will hold the service rate of each route 
    for i in range(amountOfRoutes):   
        A.append(0)
        # A.append(random.randint(1,min(math.ceil(C/2),C-sum(A))) ) #required: minimum value of 1
        arrRates.append(random.uniform(0,10)) #required: minimum value of 0
        serRates.append(1) #required: minimum value of 0
    print("route requirements")
    print(A)
    print("arrival rates")
    print(arrRates)
    

    #INPUT - Extention for supermodularity check
    subsetAmountOfRoutes = random.randint(2,amountOfRoutes-1) #required: minimum value of 2, maximum value of amountOfRoutes-1
    print("Amount of routes in subset")
    print(subsetAmountOfRoutes)
    subset_A = A[:subsetAmountOfRoutes]
    subset_arrRates = arrRates[:subsetAmountOfRoutes]
    subset_serRates = serRates[:subsetAmountOfRoutes]

    # Compute the blocking probability and rate of loss for...
    # ...The full set of routes
    block_prob = blocking_probabilities(sum(arrRates),C,A)
    print("erlang blocking probabilities=")
    print(block_prob)
    lossRate = rate_of_loss(block_prob,arrRates,serRates)
    #print("loss rate =")
    #print(lossRate)
    assert lossRate == 0, "Error: lossRate is not 0"

    # ...The subset of routes
    subset_block_prob = blocking_probabilities(sum(subset_arrRates),C,subset_A)
    print("subset erlang blocking probabilities=")
    print(subset_block_prob)
    subset_lossRate = rate_of_loss(subset_block_prob,subset_arrRates,subset_serRates)
    print("subset loss rate =")
    print(subset_lossRate)    

    # for each route belonging to the subset, remove it and see "what happens" both at the original set and at the subset.
    # three checks:
    #  is the blocking probability of a route ever increased? (comparison made between original set and original set minus route)
    #  is the rate of loss monotonic? (comparison made between original set and original set minus route)
    #  is the rate of loss supermodular? (comparison made between original set and subset)

    for i in range(subsetAmountOfRoutes):

        #Compute the blocking probabilities and loss rate
        # ...for the original set minus route i
        print("")
        print("Removing route with id=")
        print(i)
        A_new = A[0:i]
        A_new += A[i+1:]
        arrRates_new = arrRates[0:i]
        arrRates_new += arrRates[i+1:]
        serRates_new = serRates[0:i]
        serRates_new += serRates[i+1:]
        print("A_new=")
        print(A_new)
        print("arrRates_new=")
        print(arrRates_new)
        print("serRates_new=")
        print(serRates_new)

        block_prob_new = blocking_probabilities(sum(arrRates_new),C,A_new)
        print("erlang blocking probabilities new=")
        print(block_prob_new)

        lossRate_new = rate_of_loss(block_prob_new,arrRates_new,serRates_new)
        print("loss rate new =")
        print(lossRate_new)
        print("new loss rate - old loss rate = ")
        print(lossRate_new-lossRate)
        if lossRate_new>lossRate:
            print("NOT MONOTONIC")
            print("By removing route ",j," the rate of loss becomes ",lossRate_new,". Its original value was ",lossRate)
            monotonicityFlag=True
        block_prob_new.insert(i,-1) #dummy value inserted so that block_prob arrays have the same length
        for j in range(len(block_prob)):
            if i!=j and block_prob_new[j]>block_prob[j]:
                blockingFlag=True
                print("blocking probability may increase")
                print("Blocking probability of route ", j, "increased. Original value was ", block_prob[j], ", new value is ", block_prob_new[j])
        

        # ...for the subset minus route i
        # (this part is necessary to test for submodularity)
        print("")
        subset_A_new = subset_A[0:i]
        subset_A_new += subset_A[i+1:]
        subset_arrRates_new = subset_arrRates[0:i]
        subset_arrRates_new += subset_arrRates[i+1:]
        subset_serRates_new = subset_serRates[0:i]
        subset_serRates_new += subset_serRates[i+1:]
        print("subset_A_new=")
        print(subset_A_new)
        print("subset_arrRates_new=")
        print(subset_arrRates_new)
        print("subset_serRates_new=")
        print(subset_serRates_new)

        subset_block_prob_new= blocking_probabilities(sum(subset_arrRates_new),C,subset_A_new)
        print("erlang subset blocking probabilities new=")
        print(subset_block_prob_new)

        subset_lossRate_new = rate_of_loss(subset_block_prob_new,subset_arrRates_new,subset_serRates_new)
        print("subset_loss rate new =")
        print(subset_lossRate_new)
        print("subset loss rate new - subset loss rate old = ")
        print(subset_lossRate_new-subset_lossRate)
        if lossRate - lossRate_new < subset_lossRate - subset_lossRate_new:
            print('not supermodular')
            print('the decrease in the rate of loss of removing route with id ',i,'is greater in the set of fewer routes')
            supermodFlag=True


    if monotonicityFlag:
        print("NOT MONOTONIC")
    if blockingFlag:
        print("blocking probability may increase")
    if supermodFlag:
        print('not supermodular')
