import numpy as np

from loadUserData import loadUserData
from user import User


username = raw_input("Enter username (e.g. CrazyFart) : ")

print "Getting your subreddit likings..."
u = User(username, 0)
u.getScore()
u.normalizeScore()


print "Loading other users' Reddit data..."

listUsers = loadUserData()
listUsers = [u] + listUsers     # Adding new user to listUsers

listSubs = {}
for u in listUsers:
    for sub in u.normSubScore:
        if sub in listSubs:
            listSubs[sub] += 1
        else:
            listSubs[sub] = 1

listSubs = [s for s in listSubs if listSubs[s] >= 5]
# listSubs = [s for s in listSubs]

numSubs = len(listSubs)
numUsers = len(listUsers)+1
print numSubs

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

