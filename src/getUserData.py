import json

from user import User

userFile = open('../data/usersList.txt', 'r')
listUsers = userFile.readlines()
listUsers = [u.rstrip() for u in listUsers]

userDataFile = open('../data/userData.txt', 'w')

data = []
i = 1

for u in listUsers:

    try:
        # print "Getting data for user No.", i, ":", u, "..."
        newUser = User(u)
        newUser.getScore()
        newUser.normalizeScore()
        print "Extracted subreddit data for user No.", i, ":", u

        userData = {'username': u, 'data': newUser.normSubScore}
        data.append(userData)
    except:
        print "Data extraction failed for user No.", i, ":", u
    i += 1

with open('../data/userData.json', 'w') as datafile:
    json.dump(data, datafile, indent=4, ensure_ascii=False)
