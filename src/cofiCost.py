import numpy as np

def cofiCost(params, Y, R, numUsers, numSubs, numFeatures, lamda):

    # Retrieve original X and Theta from params
    X = params[:numSubs*numFeatures].reshape(numSubs, numFeatures)
    Theta = params[numSubs*numFeatures:].reshape(numUsers, numFeatures)

    # Calculate cost
    J = sum(sum(((np.dot(X, np.transpose(Theta))-Y)**2)*R))/2
    J += (lamda/2)*(sum(sum(X**2)) + sum(sum(Theta**2)))

    return J


def cofiCostGrad(params, Y, R, numUsers, numSubs, numFeatures, lamda):

    X = params[:numSubs*numFeatures].reshape(numSubs, numFeatures)
    Theta = params[numSubs*numFeatures:].reshape(numUsers, numFeatures)

    
