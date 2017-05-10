import praw
import json
import Config
from urllib2 import urlopen
from sys import argv

# Format results into Reddit format
def formatResults(result):
    tableResults = ('{} | {} | {}\n' + \
                    '{} | {} | {}\n').format('Collection', 'Artist', 'iTunes Url',
                                             '---', '---', '---')
    for i in result['results']:
        if i['wrapperType'] == 'collection':
            if 'contentAdvisoryRating' in i:
                if i['artistName'] == artistName:
                    tableResults += ('{} ({}) | **{}** | [Link]({})\n').format(
                            i['collectionName'], i['contentAdvisoryRating'],
                            i['artistName'], i['collectionViewUrl'])
                else:
                    tableResults += ('{} ({}) | *{}* | [Link]({})\n').format(
                            i['collectionName'], i['contentAdvisoryRating'],
                            i['artistName'], i['collectionViewUrl'])
            else:
                if i['artistName'] == artistName:
                    tableResults += ('{} (Clean) | **{}** | [Link]({})\n').format(
                            i['collectionName'], i['artistName'],
                            i['collectionViewUrl'])
                else:
                    tableResults += ('{} (Clean) | *{}* | [Link]({})\n').format(
                            i['collectionName'], i['artistName'],
                            i['collectionViewUrl'])
    return tableResults

# Process submission
def processSubmission(submission):


# Main method
if __name__ == "__main__":
    # Get args
    artistId = Config.artistId
    limit = Config.limit

    # Create UrlPath for iTunes API
    print 'Searching...'
    urlpath = urlopen('https://itunes.apple.com/lookup?id=' + artistId
            + '&entity=album&limit=' + limit + '&sort=recent')
    # Store JSON into result for later use and get Artist's name
    result = json.loads(urlpath.read())
    artistName = result['results'][0]['artistName']
    print 'Artist name entered: ' + artistName
    # Write to JSON file (strictly for testing purposes)
    target = open(artistName + '.json', 'w')
    target.truncate()
    print 'Writing to JSON file'
    urlpath = urlopen('https://itunes.apple.com/lookup?id=' + artistId
            + '&entity=album&limit=' + limit + '&sort=recent')
    target.write(urlpath.read())
    target.close()
    print 'Done writing to JSON file!'

    # Format information into tableResults for Reddit submission
    tableResults = formatResults(result)
    print tableResults


    """ Reddit submission here """
    titleText = artistName + '\'s ' + limit +' Most Recent iTunes Albums'
    reddit = praw.Reddit(user_agent = 'Test (by /u/mrricearoni)',
            client_id = Config.client_id,
            client_secret = Config.client_secret,
            password = Config.password,
            user_agent = 'asdf',
            username = Config.username)
    reddit.subreddit('test').submit(title = titleText, selftext = tableResults)

    # tableResults += ("{0} " + ("({1})" if 'contentAdvisoryRating' in i else "(Clean)") + \
    #         (" | **{2}**" if i['artistName'] == artistName else " | *{2}*") + \
    #         " | [Link]({3})\n").format(
    #                 i['collectionName'], i['contentAdvisoryRating'],
    #                 i['artistName'], i['collectionViewUrl'])
