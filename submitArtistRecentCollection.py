import praw
import json
import sqlite3
from urllib2 import urlopen
from sys import argv

user_password = argv[1]
artistId = argv[2]
limit = argv[3]

# Create UrlPath for iTunes API
print 'Searching...'
urlpath = urlopen('https://itunes.apple.com/lookup?id=' + artistId
        + '&entity=album&limit=' + str(limit) + '&sort=recent')
# Store JSON into result for later use and get Artist's name
result = json.loads(urlpath.read())
artistName = result['results'][0]['artistName']
print 'Artist name entered: ' + artistName
# Write to JSON file (strictly for testing purposes)
target = open(artistName + '.json', 'w')
target.truncate()
print 'Writing to JSON file'
urlpath = urlopen('https://itunes.apple.com/lookup?id=' + artistId
        + '&entity=album&limit=' + str(limit) + '&sort=recent')
target.write(urlpath.read())
target.close()
print 'Done writing to JSON file!'

# Format information into tableResults for Reddit submission
tableResults = ('{} | {} | {}\n' + \
                '{} | {} | {}\n').format('Collection', 'Artist', 'iTunes Url',
                                         '---', '---', '---')
for i in result['results']:
    if i['wrapperType'] == 'collection':
        if 'contentAdvisoryRating' in i:
            if i['artistName'] == artistName:
                tableResults += ('{} ({}) | **{}** | [Link]({})\n').format(
                        i['collectionName'], i['contentAdvisoryRating'],
                        i['artistName'], i['collectionViewUrl']
                )
            else:
                tableResults += ('{} ({}) | *{}* | [Link]({})\n').format(
                        i['collectionName'], i['contentAdvisoryRating'],
                        i['artistName'], i['collectionViewUrl']
                )
        else:
            if i['artistName'] == artistName:
                tableResults += ('{} (Clean) | **{}** | [Link]({})\n').format(
                        i['collectionName'], i['artistName'],
                        i['collectionViewUrl']
                )
            else:
                tableResults += ('{} (Clean) | *{}* | [Link]({})\n').format(
                        i['collectionName'], i['artistName'],
                        i['collectionViewUrl']
                )

""" Reddit submission here """
titleText = artistName + '\'s ' + str(limit) +' Most Recent iTunes Albums'
reddit = praw.Reddit(client_id = '',
        client_secret = '',
        password = user_password,
        user_agent = 'asdf',
        username = '')
reddit.subreddit('').submit(title = titleText, selftext = tableResults)
