import numpy as np

from loadUserData import loadUserData
from user import User

listUsers = loadUserData()

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
numUsers = len(listUsers)
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

