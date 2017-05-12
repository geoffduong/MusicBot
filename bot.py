import praw
import Config

# String templates
QUESTIONS = ["mirror"]
REPLY_TEMPLATE = "[SoundCloud Mirror]({})"

def main():

    # Initialize Reddit instance
    reddit = praw.Reddit(user_agent = 'Test',
            client_id = Config.client_id,
            client_secret = Config.client_secret,
            password = Config.password,
            username = Config.username)

    # Join subreddits
    subreddits = reddit.subreddit("+".join(Config.subreddits))
    print subreddits

    # TESTING BOT HERE
    # Testing on single thread-------------------------------------------------
    # thread = "https://www.reddit.com/r/hiphopheads/comments/6ae0d3/fresh_quavo_paper_over_here/"
    # submission = reddit.submission(url=thread)
    # submission.comments.replace_more(limit=0)
    # for comment in submission.comments.list():
    #     text = comment.body
    #     text = text.lower()
    #     comment_parsed = text.split(" ")
    #     for word in comment_parsed:
    #         if word in QUESTIONS:
    #             reply_text = REPLY_TEMPLATE.format("https://soundcloud.com/ogxparker/quavo-paper-over-here-prod-og-parker#t=0:00")
    #             comment.reply(reply_text)
    #             break
    # -------------------------------------------------------------------------

    # Testing on a subreddit---------------------------------------------------
    for comment in subreddits.stream.comments():
        text = comment.body.lower()
        comment_parsed = text.split(" ")
        for word in comment_parsed:
            if word in QUESTIONS:
                print text, comment.submission.shortlink
        # print comment.body, comment.submission.shortlink
    # -------------------------------------------------------------------------
    
# Main method
if __name__ == "__main__":
    main()
