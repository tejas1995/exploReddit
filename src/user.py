import praw
import math

from tabulate import tabulate
from sigmoid import sig


class User:

    def __init__(self, username):

        r = praw.Reddit(user_agent = 'new_redditor')
        self.username = username
        self.user = r.get_redditor(self.username)
        self.subScore = {}


    def getScore(self):

        subm = self.user.get_submitted(limit=None)
        for s in subm:
            if s.subreddit.display_name in self.subScore:
                self.subScore[s.subreddit.display_name] += 2*s.score
            else:
                self.subScore[s.subreddit.display_name] = 2*s.score

        comt = self.user.get_comments(limit=None)
        for c in comt:
            if c.subreddit.display_name in self.subScore:
                self.subScore[c.subreddit.display_name] += c.score
            else:
                self.subScore[c.subreddit.display_name] = c.score


    def normalizeScore(self):

        self.normSubScore = {}
        for sub, score in self.subScore.iteritems():
            self.normSubScore[sub] = 5*sig(-4+8*score/500)

    def printScore(self):

        table = []
        for key, val in self.subScore.iteritems():
            table.append([key, val, self.normSubScore[key]])
            # print 'Subreddit:', key, '\tScore:', val, '\tNormalized:', 
            # print "%.2f" % self.normSubScore[key]
        print tabulate(table)
