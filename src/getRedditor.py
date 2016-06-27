from user import User

username = raw_input("Enter username (e.g. CrazyFart) : ")

u = User(username)
u.getScore()
u.normalizeScore()
u.printScore()

