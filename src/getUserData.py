import time
import requests
import requests.auth
import praw
from bs4 import BeautifulSoup
from urllib2 import urlopen, Request
import urllib

inputFile = open('../data/popularSubs.txt', 'r')

subList = inputFile.readlines()
subList = [sub.rstrip() for sub in subList]

listUsers = []

# Set base URLs
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

def makeSoup(url):

    hdr = {'User-Agent': user_agent,
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           }
    req = Request(url, headers=hdr)
    html = urlopen(req).read()
    soup = BeautifulSoup(html, "lxml")
    return soup


for sub in subList:

    topUrl = 'http://www.reddit.com/r/' + sub + '/top/?sort=top&t=month'
    soup = makeSoup(topUrl)

    print "Subreddit:", sub
    print "---------------------------"

    for i in range(1, 11):
        try:
            topDiv = soup.find(attrs={"data-rank": str(i)})
            topDivOP = topDiv.find('p', attrs={"class": "tagline"}).find("a").string
 
            if (topDivOP not in listUsers) is True:
                print topDivOP
                listUsers.append(topDivOP)
        except:
            break

print len(listUsers)

userFile = open('../data/usersList.txt', 'w')
for user in listUsers:
    userFile.write(user + '\n')
