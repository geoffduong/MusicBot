import json
import time
from urllib2 import urlopen
import praw
from sys import argv

user_password = argv[1]
albumID = argv[2]
titleHeader = argv[3]

reddit = praw.Reddit(client_id = '',
        client_secret = '',
        password = user_password,
        user_agent = 'asdf',
        username = '')

urlpath = urlopen('https://itunes.apple.com/lookup?id=' + albumID)
result = json.loads(urlpath.read())

count = 0
while result['resultCount'] == 0:
    urlpath = urlopen('https://itunes.apple.com/lookup?id=' + albumID)
    result = json.loads(urlpath.read())
    print count, (result['resultCount'])
    count = count + 1
    time.sleep(3)

titleText = titleHeader + result['results'][0]['collectionName'] + ' - ' + result['results'][0]['artistName']
reddit.subreddit('').submit(title = titleText,
        url = result['results'][0]['collectionViewUrl'])
