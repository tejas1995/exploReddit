import numpy as np


def normalizedScore(score):

    if(score <= 0):
        return 0
    elif score > 0 and score <= 20:
        return round((score)/20.0, 2)
    elif score > 20 and score <= 80:
        return 1 + round((score-20)/60.0, 2)
    elif score > 80 and score <= 175:
        return 2 + round((score-80)/95.0, 2)
    elif score > 175 and score <= 300:
        return 3 + round((score-175)/125.0, 2)
    elif score >= 300 and score < 500:
        return 4 + round((score-300)/200.0, 2)
    elif score > 500:
        return 5

def normalizeRatings(Y, R):

    numSubs = Y.shape[0]
    numUsers = Y.shape[1]

    normY = np.zeros((numSubs, numUsers))
    meanY = np.zeros(numSubs)

    for i in range(numSubs):
        numRatings = R[i].nonzero()[0].size
        if numRatings is 0:
            meanY[i] = 0
        else:
            meanY[i] = round(sum(Y[i]*R[i])/numRatings, 2)
        normY[i] = Y[i] - meanY[i]

    return [normY, meanY]
