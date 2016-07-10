import numpy as np

def cofiCost(params, Y, R, numUsers, numSubs, numFeatures, lamda):

    # Retrieve original X and Theta from params
    X = params[:numSubs*numFeatures].reshape(numSubs, numFeatures)
    Theta = params[numSubs*numFeatures:].reshape(numUsers, numFeatures)

    # Calculate cost
    J = sum(sum(((X.dot(Theta.T)-Y)**2)*R))/2
    J += (lamda/2)*(sum(sum(X**2)) + sum(sum(Theta**2)))

    print "Cost:", J

    return J


def cofiCostGrad(params, Y, R, numUsers, numSubs, numFeatures, lamda):

    X = params[:numSubs*numFeatures].reshape(numSubs, numFeatures)
    Theta = params[numSubs*numFeatures:].reshape(numUsers, numFeatures)

    X_grad = np.zeros((numSubs, numFeatures))
    Theta_grad = np.zeros((numUsers, numFeatures))

    for i in range(numSubs):
        X_grad[i] = ((X[i].dot(Theta.T) - Y[i])*R[i]).dot(Theta)
        X_grad[i] += lamda*X[i]

    for i in range(numUsers):
        Theta_grad[i] = (X.T.dot((X.dot(Theta.T[:,i]) - Y[:,i])*R[:,i])).T
        Theta_grad[i] += lamda*Theta[i]

    res = np.concatenate((np.array(X_grad).ravel(), np.array(Theta_grad).ravel()))

    return res 

    
