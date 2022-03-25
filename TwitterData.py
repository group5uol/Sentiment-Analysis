from textblob import TextBlob
import sys
import tweepy
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import pycountry
import re
import string
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer

#Authentication for Twitter API
consumerKey         =   "YdqYR73XZ6sbCXBZJ9GAoZjOI"
consumerSecret      =   "oLHLHD33Uqc6OGjyX4LMCoAS0dRURYLT1pz3VaLpI4XXo6JRxe"
accessToken         =   "1505907787859173381-4nzm4Xeq6bHQRRKmOY1vWl4pvKBdqN"
accessTokenSecret   =   "J5xHHgjZrbMJWMv52bb5zTJwTZoRu9aDQy5fOggYM377Y"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

#Getting Tweets With Keyword or Hashtag
def percentage(part, whole):
    return 100 * float(part) / float(whole)

keyword = "covid-19"
noOfTweet = "10"

tweets = tweepy.Cursor(api.search_tweets, q=keyword).items(noOfTweet)
positive = 0
negative = 0
neutral = 0
polarity = 0
tweet_list = []
neutral_list = []
negative_list = []
positive_list = []

for tweet in tweets:
    tweet_list.append(tweet.text)
    analysis = TextBlob(tweet.text)
    nltk.download('vader_lexicon')
    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(tweet.text)
    neg = score['neg']
    neu = score['neu']
    pos = score['pos']
    comp = score['compound']
    polarity += analysis.sentiment.polarity

    if neg > pos:
        negative_list.append(tweet.text)
        negative += 1
    elif pos > neg:
        positive_list.append(tweet.text)
        positive += 1
    elif pos == neg:
        neutral_list.append(tweet.text)
        neutral += 1

    positive = percentage(positive, noOfTweet)
    negative = percentage(negative, noOfTweet)
    neutral  = percentage(neutral, noOfTweet)
    polarity = percentage(polarity, noOfTweet)

    positive = float(format(positive, '.1f'))
    negative = float(format(negative, '.1f'))
    neutral  = float(format(neutral, '.1f'))

# visualising the data
tweet_list = pd.DataFrame(tweet_list)
neutral_list = pd.DataFrame(neutral_list)
negative_list = pd.DataFrame(negative_list)
positive_list = pd.DataFrame(positive_list)
print("total number: ",len(tweet_list))
print(tweet_list.values)
print("positive number: ",len(positive_list))
print("negative number: ", len(negative_list))
print("neutral number: ",len(neutral_list))

#write data to local file
filename = "static/analysis.csv"
tweet_list.to_csv(filename, index = False) #
print('Scrapping Done')

#cleaning the data