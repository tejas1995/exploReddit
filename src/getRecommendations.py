import numpy as np
import random

from scipy import optimize

from loadUserData import loadUserData
from user import User, checkUserExistence
from normalize import normalizedScore, normalizeRatings
from cofiCost import cofiCost, cofiCostGrad

# Load list of training set users
listUsers = loadUserData()

# Getting a valid username
usernameValid = False
while usernameValid is False:
    username = raw_input("Enter username (e.g. CrazyFart) : ")
    if checkUserExistence(username) is True:
        usernameValid = True
    else:
        print "Invalid username! Try again"

# If username is not in training set, make new user and add to list
if username not in [u.username for u in listUsers]:
    print "Identifying your subreddit tastes..."
    u = User(username, len(listUsers))
    u.getScore()
    u.normalizeScore()
    listUsers.append(u)     # Adding new user to listUsers 


print "Loading other users' Reddit data..."

listSubs = {}
for u in listUsers:
    for sub in u.normSubScore:
        if sub in listSubs:
            listSubs[sub] += 1
        else:
            listSubs[sub] = 1

# Get list of subs with at least 5 users in training set using it
listSubs = [str(s) for s in listSubs if listSubs[s] >= 5]

# Set parameters numSubs, numUsers
numSubs = len(listSubs)
numUsers = len(listUsers)

# Set R(i, j) = 1 if sub i has been used by user j
# Set Y(i, j) = normalized score of sub i for user j
R = np.zeros((numSubs, numUsers))
Y = np.zeros((numSubs, numUsers))

for u in listUsers:
    for i, s in enumerate(u.normSubScore):
        if s in listSubs:
            j = u.id
            Y[i][j] = u.normSubScore[s]
            R[i][j] = 1

# Get normalized Y (normY) and meanY
normed = normalizeRatings(Y, R)
normY = normed[0]
meanY = normed[1]

numFeatures = 10

print "Finding new subreddits for you to shitpost on"

# Initialize X and Theta to small random values in [0.1)
X = np.zeros((numSubs, numFeatures))
Theta = np.zeros((numUsers, numFeatures))

for i in range(numSubs):
    for j in range(numFeatures):
        X[i][j] = random.random()

for i in range(numUsers):
    for j in range(numFeatures):
        Theta[i][j] = random.random()

# Combine initial X and Theta
initParams = np.concatenate((np.array(X).ravel(), np.array(Theta).ravel()))

# Set regularization parameter
lamda = 10

costArgs = (Y, R, numUsers, numSubs, numFeatures, lamda)

optimParams = optimize.fmin_cg(cofiCost, initParams, fprime=cofiCostGrad, args=costArgs, maxiter=50)

X = optimParams[:numSubs*numFeatures].reshape(numSubs, numFeatures)
Theta = optimParams[numSubs*numFeatures:].reshape(numUsers, numFeatures)

print "Recommender system learning completed"


