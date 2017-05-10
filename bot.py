import praw
import Config

def main():
    reddit = praw.Reddit(user_agent = 'Test (by /u/mrricearoni)',
            client_id = Config.client_id,
            client_secret = Config.client_secret,
            password = Config.password,
            username = Config.username)
    subreddits = reddit.subreddit("+".join(Config.subreddits))
    print subreddits
    for comment in reddit.subreddit('test').stream.comments():
        print comment.body

# Main method
if __name__ == "__main__":
    main()
