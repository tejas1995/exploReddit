import numpy as np

from loadUserData import loadUserData
from user import User, checkUserExistence

# Load list of training set users
listUsers = loadUserData()

# Getting a valid username
usernameValid = False
while usernameValid is False:
    username = raw_input("Enter username (e.g. CrazyFart) : ")
    if checkUserExistence(username) is True:
        usernameValid = True

# If username is not in training set, make new user and add to list
if username not in [u.username for u in listUsers]:
    print "Getting your subreddit likings..."
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

listSubs = [s for s in listSubs if listSubs[s] >= 5]
numSubs = len(listSubs)
numUsers = len(listUsers)

R = np.zeros((numSubs, numUsers))
Y = np.zeros((numSubs, numUsers))

for u in listUsers:
    for s in u.normSubScore:
        if s in listSubs:
            i = listSubs.index(s)
            j = u.id
            Y[i][j] = u.normSubScore[s]
            R[i][j] = 1

print Y[0]

