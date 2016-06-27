import praw
import math

from tabulate import tabulate
from normalizeScore import normalized

class User:

    def __init__(self, username):

        r = praw.Reddit(user_agent = 'new_redditor')
        self.username = username
        self.user = r.get_redditor(self.username)
        self.subScore = {}


    def getScore(self):

        self.totalScore = 0

        try:
            subm = self.user.get_submitted(limit=None)
            for s in subm:
                if s.subreddit.display_name in self.subScore:
                    self.subScore[s.subreddit.display_name] += s.score
                else:
                    self.subScore[s.subreddit.display_name] = s.score
                self.totalScore += s.score

            comt = self.user.get_comments(limit=None)
            for c in comt:
                if c.subreddit.display_name in self.subScore:
                    self.subScore[c.subreddit.display_name] += c.score
                else:
                    self.subScore[c.subreddit.display_name] = c.score
                self.totalScore += c.score
        except praw.errors.NotFound:
            print "User does not exist!"

        print "Total Score:", self.totalScore


    def normalizeScore(self):

        self.normSubScore = {}
        for sub, score in self.subScore.iteritems():
            self.normSubScore[sub] = normalized(score)

    def printScore(self):

        table = []
        for key, val in self.subScore.iteritems():
            table.append([key, val, self.normSubScore[key]])
        table.sort(key = lambda x: x[2])
        print tabulate(table)
