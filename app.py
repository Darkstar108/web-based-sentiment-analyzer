from flask import Flask, jsonify, redirect, render_template, request
import praw
import tweepy
from analysis import subredditAnalysis, userTweetAnalysis, searchTweetAnalysis, customTextAnalysis

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# To avoid caching of static files
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Render routes
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/reddit')
def reddit():
    return render_template("reddit.html")

@app.route('/twitter')
def twitter():
    return render_template("twitter.html")

@app.route('/instagram')
def instagram():
    return render_template("instagram.html")
    
@app.route('/custom')
def custom():
    return render_template("custom.html")    

@app.route('/analyse')
def analyse(template):
    return render_template(template)  

# Validation routes
@app.route('/redditValidate')
def redditValidate():
    # Connect with Reddit API
    reddit = praw.Reddit(client_id = "F7wsA_lS5CIW_g", 
                     client_secret = "TTqI5XAZk_ev3gQ4bPOwwQIAaVA", 
                     user_agent = "subSentiment")

    subreddit = request.args.get("subreddit")
    sub_exists = True

    try:
        reddit.subreddits.search_by_name(subreddit, exact=True)
    except:
        sub_exists = False

    if sub_exists and len(subreddit) > 0: 
        return jsonify(exists='T')
    else:
        return jsonify(exists='F')

@app.route('/twitterValidate')
def twitterValidate():
    # Connecting to Twitter API through Tweepy
    consumer_key = "sXdhpHvRBdLsbkzcuEjxI7l8L"
    consumer_secret = "29PO4f3p1SC2ncdF6SCCrflSqTcDrCj6MTcU0p8TNW7ZvPFYUE"
    access_token = "2986786057-RlhQduo1TE8fk71Kn88B35KozMyIAAoi5CkvVN8"
    access_token_secret = "KMSDDdi55UG6FoDMKKjghNsOAsb9xczd2R1dAaABYQ8LQ"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    valid = True

    if request.args.get("key") == 'user':
        try:
            api.get_user(screen_name=request.args.get("value"))
        except:
            valid = False
    else:
        try:
            tweets = tweepy.Cursor(api.search, q="#"+request.args.get("value")).items(1)
        except:
            valid = False

    if valid:
        return jsonify(exists='T')
    else:
        return jsonify(exists='F')

# Analysis routes
@app.route('/redditAnalyse')
def redditAnalyse():
    subreddit = request.args.get("subreddit")
    timeframe = request.args.get("timeframe")  

    polarity, subjectivity = subredditAnalysis(subreddit, timeframe)

    return jsonify(polarity=polarity, subjectivity=subjectivity)

@app.route('/twitterAnalyse')
def twitterAnalyse():
    if request.args.get("key") == 'user':
        polarity, subjectivity = userTweetAnalysis(request.args.get("value"), int(request.args.get("count")))
    else:
        polarity, subjectivity = searchTweetAnalysis(request.args.get("value"), int(request.args.get("count")))

    return jsonify(polarity=polarity, subjectivity=subjectivity)

@app.route('/customTextAnalyse')
def customTextAnalyse():
    polarity, subjectivity = customTextAnalysis(request.args.get("text"))

    return jsonify(polarity=polarity, subjectivity=subjectivity)
        