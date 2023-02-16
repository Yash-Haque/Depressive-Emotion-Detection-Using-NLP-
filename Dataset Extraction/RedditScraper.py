import praw
import config
import pandas as pd

reddit = praw.Reddit(
    client_id=config.REDDIT_ID,
    client_secret=config.REDDIT_SECRET,
    password=config.REDDIT_PASS,
    user_agent="USERAGENT",
    username=config.REDDIT_USER,
)
heading = []
iden = []
autho = []
utc = []
sco = []
upvr = []
body = []
link = []

heading.append('TITLE')
iden.append('POST-ID')
autho.append('AUTHOR')
utc.append('CREATED TIME') 
sco.append('SCORE') 
upvr.append('UPVOTE RATIO')
body.append('BODY')
link.append('URL')



for submissions in reddit.subreddit('depression').hot(limit=None):

        heading.append(submissions.title)
        iden.append(submissions.id)
        autho.append(submissions.author)
        utc.append(submissions.created_utc) 
        sco.append(submissions.score)
        upvr.append(submissions.upvote_ratio)
        body.append(submissions.selftext)
        link.append(submissions.url)


data = {
    'TITLE':heading,
    'ID':iden,
    'AUTHOR':autho,
    'CREATED TIME':utc, 
    'SCORE':sco,
    'UPVOTE RATIO':upvr,
    'BODY':body,
    'URL':link
}

print(data)
print(len(data))

dataframe = pd.DataFrame(data)
# dataframe.head()
dataframe.to_csv('submissionsTrial.csv', header=False, encoding='utf-8',index=False)