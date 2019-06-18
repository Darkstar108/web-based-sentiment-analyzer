# web-based-sentiment-analyzer

A basic webapp written in python using flask that analyses sentiment of text from Reddit, Twitter and any custom text entered.

It interacts with Reddit through praw to get comments for analysis from a choosen subreddit in a given timeframe. It interacts with Twitter through tweepy to get tweets from a selected user or from a selected hashtag. All analysis is done using the Textblob package.

app.py contains the web framework and the analysis is done in analysis.py.

All webpages have been made using Bootstrap and the graphs have been constructed using Chartjs
