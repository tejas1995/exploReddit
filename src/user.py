import praw

class User:

    def __init__(self, username):

        r = praw.Reddit(user_agent = 'new_redditor')
        self.username = username
        self.user = r.get_redditor(self.username)
        self.subScore = {}

        print '----------------------------'

   
    def getScore(self):

        subm = self.user.get_submitted(limit=None)
        for s in subm:
            if s.subreddit.display_name in self.subScore:
                self.subScore[s.subreddit.display_name] += 5*s.score
            else:
                self.subScore[s.subreddit.display_name] = 5*s.score

        comt = self.user.get_comments(limit=None)
        for c in comt:
            if c.subreddit.display_name in self.subScore:
                self.subScore[c.subreddit.display_name] += c.score
            else:
                self.subScore[c.subreddit.display_name] = c.score


    def printScore(self):

        for key, val in self.subScore.iteritems():
            print 'Subreddit:', key, '\tScore:', val
