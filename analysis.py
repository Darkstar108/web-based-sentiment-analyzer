import praw
import tweepy
from textblob import TextBlob
import math

# Analyse comments of a subreddit
def subredditAnalysis(subreddit, timeframe):
    # Connenct with Reddit API
    reddit = praw.Reddit(client_id = "F7wsA_lS5CIW_g", 
                     client_secret = "TTqI5XAZk_ev3gQ4bPOwwQIAaVA", 
                     user_agent = "subSentiment")

    polarity = 0
    subjectivity = 0
    num_comments = 0
    
    # For each non sticky submission in the given subreddit and timeframe calculate polarity and subjectivity of comments
    for submission in reddit.subreddit(subreddit).top(timeframe):
        if not submission.stickied:
            submission.comments.replace_more(limit=0)

            for comment in submission.comments.list():
                comment_sentiment = TextBlob(comment.body)
                  
                polarity += comment_sentiment.sentiment.polarity
                subjectivity += comment_sentiment.sentiment.subjectivity
                num_comments += 1
    
    if num_comments == 0:
        return 0, 0

    polarity = polarity/num_comments
    subjectivity = (subjectivity/num_comments)-0.5

    return polarity, subjectivity

# Analyse tweets of a user
def userTweetAnalysis(user, count):
    # Connecting to Twitter API through Tweepy
    consumer_key = "sXdhpHvRBdLsbkzcuEjxI7l8L"
    consumer_secret = "29PO4f3p1SC2ncdF6SCCrflSqTcDrCj6MTcU0p8TNW7ZvPFYUE"
    access_token = "2986786057-RlhQduo1TE8fk71Kn88B35KozMyIAAoi5CkvVN8"
    access_token_secret = "KMSDDdi55UG6FoDMKKjghNsOAsb9xczd2R1dAaABYQ8LQ"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    polarity = 0
    subjectivity = 0
    num_tweets = 0

    # For selected number of tweets by selected user calculate polarity and subjectivity
    for tweet in tweepy.Cursor(api.user_timeline, screen_name = user).items(count):
        tweet_sentiment = TextBlob(tweet.text)

        num_tweets += 1
        polarity += tweet_sentiment.sentiment.polarity
        subjectivity += tweet_sentiment.sentiment.subjectivity 

    if num_tweets == 0:
        return 0, 0

    polarity = polarity/num_tweets
    subjectivity = (subjectivity/num_tweets)-0.5

    return polarity, subjectivity

# Analyse tweets by topic
def searchTweetAnalysis(topic, count):
    # Connecting to Twitter API through Tweepy
    consumer_key = "sXdhpHvRBdLsbkzcuEjxI7l8L"
    consumer_secret = "29PO4f3p1SC2ncdF6SCCrflSqTcDrCj6MTcU0p8TNW7ZvPFYUE"
    access_token = "2986786057-RlhQduo1TE8fk71Kn88B35KozMyIAAoi5CkvVN8"
    access_token_secret = "KMSDDdi55UG6FoDMKKjghNsOAsb9xczd2R1dAaABYQ8LQ"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    polarity = 0
    subjectivity = 0
    num_tweets = 0

    # For selected number of tweets on selected topic calculate polarity and subjectivity
    for tweet in tweepy.Cursor(api.search, q="#" + topic).items(count):
        tweet_sentiment = TextBlob(tweet.text)

        num_tweets += 1
        polarity += tweet_sentiment.sentiment.polarity
        subjectivity += tweet_sentiment.sentiment.subjectivity 

    if num_tweets == 0:
        return 0, 0

    polarity = polarity/num_tweets
    subjectivity = (subjectivity/num_tweets)-0.5

    return polarity, subjectivity

# Analyse custom text
def customTextAnalysis(text):
    polarity = 0
    subjectivity = 0

    text_sentiment = TextBlob(text)
    polarity = text_sentiment.sentiment.polarity
    subjectivity = text_sentiment.sentiment.subjectivity-0.5

    return polarity, subjectivity