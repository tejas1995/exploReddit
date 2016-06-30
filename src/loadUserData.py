import json
from user import User

def loadUserData():
    jsonData = open('../data/userData.json', 'r').read()

    userData = json.loads(jsonData)

    listUsers = []

    for data in userData:
        
        u = User(data['username'], len(listUsers)+1)
        u.setNormScore(data['data'])
        # print "User", u.username
        # u.printScore()
        # raw_input("Press Enter to continue...")
        listUsers.append(u)

    return listUsers
