import praw
import math

from tabulate import tabulate
from normalizeScore import normalized

class User:

    def __init__(self, username, id):

        r = praw.Reddit(user_agent = 'new_redditor')
        self.username = username
        self.subScore = {}
        self.normSubScore = {}
        self.id = id


    def getScore(self):

        self.user = r.get_redditor(self.username)
        self.totalScore = 0

        try:
            subm = self.user.get_submitted(limit=200)
            for s in subm:
                if s.subreddit.display_name in self.subScore:
                    self.subScore[s.subreddit.display_name] += s.score
                else:
                    self.subScore[s.subreddit.display_name] = s.score
                self.totalScore += s.score

            comt = self.user.get_comments(limit=500)
            for c in comt:
                if c.subreddit.display_name in self.subScore:
                    self.subScore[c.subreddit.display_name] += c.score
                else:
                    self.subScore[c.subreddit.display_name] = c.score
                self.totalScore += c.score

        except praw.errors.NotFound:
            print "User does not exist!"


    def normalizeScore(self):

        for sub, score in self.subScore.iteritems():
            self.normSubScore[sub] = normalized(score)


    def setNormScore(self, normScoreDict):

        self.normSubScore = normScoreDict


    def printScore(self):

        table = []
        for key, val in self.normSubScore.iteritems():
            table.append([key, val])
        table.sort(key = lambda x: x[1])
        print tabulate(table)
