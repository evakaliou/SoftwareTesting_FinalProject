from .blockProbs.blockProbs_v1 import blocking_probabilities
from .rateLoss.rateLoss_v1 import rate_of_loss


def supermod_check(C, A, arrRates, serRates, subsetAmountOfRoutes):

    block_prob = blocking_probabilities(sum(arrRates), C, A)
    lossRate = rate_of_loss(block_prob, arrRates, serRates)

    subset_A = A[:subsetAmountOfRoutes]
    subset_arrRates = arrRates[:subsetAmountOfRoutes]
    subset_serRates = serRates[:subsetAmountOfRoutes]
    # Compute the blocking probability and rate of loss for
    # the subset of routes
    subset_block_prob = blocking_probabilities(sum(subset_arrRates), C, subset_A)
    subset_lossRate = rate_of_loss(subset_block_prob, subset_arrRates, subset_serRates)

    # for each route belonging to the subset,
    #  remove it and see "what happens" both at the original set and at the subset:
    #  is the rate of loss supermodular? (comparison made between original set and subset)
    for i in range(subsetAmountOfRoutes):
        # Compute the blocking probabilities and loss rate
        # ...for the original set minus route i
        A_new = A[0:i]
        A_new += A[i + 1:]
        arrRates_new = arrRates[0:i]
        arrRates_new += arrRates[i + 1:]
        serRates_new = serRates[0:i]
        serRates_new += serRates[i + 1:]
        block_prob_new = blocking_probabilities(sum(arrRates_new), C, A_new)
        lossRate_new = rate_of_loss(block_prob_new, arrRates_new, serRates_new)
        # ...for the subset minus route i
        subset_A_new = subset_A[0:i]
        subset_A_new += subset_A[i + 1:]
        subset_arrRates_new = subset_arrRates[0:i]
        subset_arrRates_new += subset_arrRates[i + 1:]
        subset_serRates_new = subset_serRates[0:i]
        subset_serRates_new += subset_serRates[i + 1:]
        subset_block_prob_new = blocking_probabilities(sum(subset_arrRates_new), C, subset_A_new)
        subset_lossRate_new = rate_of_loss(subset_block_prob_new, subset_arrRates_new, subset_serRates_new)

        if lossRate - lossRate_new < subset_lossRate - subset_lossRate_new:
            print('not supermodular')
            print('the decrease in the rate of loss of removing route with id ', i,
                  'is greater in the set of fewer routes')
            return False

    return True
