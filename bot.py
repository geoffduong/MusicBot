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

    # Testing bot
    thread = "https://www.reddit.com/r/hiphopheads/comments/6ae0d3/fresh_quavo_paper_over_here/"
    submission = reddit.submission(url=thread)
    # comments = submission.comments.replace_more(limit=0)
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        text = comment.body
        text = text.lower()
        comment_parsed = text.split(" ")
        for word in comment_parsed:
            if word in QUESTIONS:
                reply_text = REPLY_TEMPLATE.format("https://soundcloud.com/ogxparker/quavo-paper-over-here-prod-og-parker#t=0:00")
                comment.reply(reply_text)
                break
        # print comment_parsed
        # for word in comment_parsed:
        #     if word in QUESTIONS:
                # reply_text = REPLY_TEMPLATE.format("https://soundcloud.com/ogxparker/quavo-paper-over-here-prod-og-parker#t=0:00")
                # comment.reply(reply_text)
        #     else:
        #         print False
        # if comment.body in QUESTIONS:
            # reply_text = REPLY_TEMPLATE.format("https://soundcloud.com/ogxparker/quavo-paper-over-here-prod-og-parker#t=0:00")
            # comment.reply(reply_text)

    # for comment in submission.comments:
    #     print comment.body

    # for comment in reddit.subreddit('test').stream.comments():
    #     print comment.body

# Main method
if __name__ == "__main__":
    main()
