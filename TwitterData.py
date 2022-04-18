from textblob import TextBlob
import sys
import tweepy
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import time
from datetime import datetime, date, timedelta
# Tweet pre-processor
import preprocessor as p
import pycountry
import re
import string
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer

# Generate list of dates (7 days window) based on today's date
list_of_dates = []
today = date.today()
for i in range(-7,1):
    target_date = (today + timedelta(days=i)).strftime("%Y-%m-%d")
    list_of_dates.append(target_date)

list_of_dicts = []
search_term = 'covid19 covid vaccine'
num_tweets = 100

def get_tweets(search_term=search_term, num_tweets=num_tweets):
    for end_date in list_of_dates:
        start_date = (datetime.strptime(end_date, '%Y-%m-%d') - timedelta(days=1)).strftime(
            "%Y-%m-%d")  # Create 1-day windows for extraction
        tweet_count = len(list_of_dicts)

        for tweet in tweepy.Cursor(api.search_tweets,
                                   q=f'{search_term} since:{start_date} until:{end_date}',
                                   lang='en',
                                   count=num_tweets,
                                   tweet_mode='extended').items(num_tweets):
            if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
                if tweet.lang == "en":
                    tweet_dict = {}
                    tweet_dict['username'] = tweet.user.name
                    tweet_dict['location'] = tweet.user.location
                    tweet_dict['text'] = tweet.full_text
                    # tweet_dict['fav_count'] = tweet.favorite_count
                    tweet_dict['hashtags'] = tweet.entities['hashtags']
                    tweet_dict['tweet_date'] = tweet.created_at
                    list_of_dicts.append(tweet_dict)
                    tweet_count += 1
                   # print(f'Extracted tweet count = {tweet_count}')

        print(f'Completed extraction for {start_date} to {end_date},extracted tweet count = {tweet_count}.')
        #time.sleep(100)
        print('Ready to go again')

    print(len(list_of_dicts))

# Setup function to extract hashtags text from the raw hashtag dictionaries
def extract_hashtags(hashtag_list):
    s = ""  # Create empty string
    if not hashtag_list:  # If list is empty, return empty string
        return s
    else:
        for dictionary in hashtag_list:
            s += str(dictionary['text'].lower() + ',')  # Create string (lowercase) for each hashtag text
        s = s[:-1]  # Drop last character ','
        return s

#Text Pre-processing
def dataClean(tweets_df):
    # Clean tweet text with tweet-preprocessor
    tweets_df['text_cleaned'] = tweets_df['text'].apply(lambda x: p.clean(x))
    # Remove duplicate tweets
    tweets_df.drop_duplicates(subset='text_cleaned', keep="first", inplace=True)
    len(tweets_df)
    # Remove unnecessary characters
    # Note: Need to remove % as Stanford CoreNLP annotation encounters error if text contains some of these characters
    punct = ['%', '/', ':', '\\', '&amp;', '&', ';']

    def remove_punctuations(text):
        for punctuation in punct:
            text = text.replace(punctuation, '')
        return text

    tweets_df['text_cleaned'] = tweets_df['text_cleaned'].apply(lambda x: remove_punctuations(x))

    # Drop tweets which have empty text field
    tweets_df['text_cleaned'].replace('', np.nan, inplace=True)
    tweets_df['text_cleaned'].replace(' ', np.nan, inplace=True)
    tweets_df.dropna(subset=['text_cleaned'], inplace=True)

    tweets_df = tweets_df.reset_index(drop=True)


if __name__ == '__main__':

    pd.set_option('display.max_columns', 20)  # 给最大列设置为10列
    pd.set_option('display.max_rows', 100)  # 设置最大可见100行

    # Authentication for Twitter API
    consumerKey = "YdqYR73XZ6sbCXBZJ9GAoZjOI"
    consumerSecret = "oLHLHD33Uqc6OGjyX4LMCoAS0dRURYLT1pz3VaLpI4XXo6JRxe"
    accessToken = "1505907787859173381-4nzm4Xeq6bHQRRKmOY1vWl4pvKBdqN"
    accessTokenSecret = "J5xHHgjZrbMJWMv52bb5zTJwTZoRu9aDQy5fOggYM377Y"

    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(auth)

    get_tweets()

    # Transform list of dictionaries into a Pandas dataframe
    tweets_df = pd.DataFrame(list_of_dicts)
    tweets_df.sort_values(by='tweet_date').reset_index(drop=True)

    # Extract hashtags
    tweets_df['hashtags_extracted'] = tweets_df['hashtags'].apply(lambda x: extract_hashtags(x))
    tweets_df.drop(columns='hashtags', inplace=True)

    dataClean(tweets_df)

    print("writting the data into local file.....ing")
    # Create timestamp for datetime of extraction
    extract_datetime = datetime.today().strftime('%Y%m%d_%H%M%S')

    # Create csv filename
    filename = 'data/covid_vaccine_tweets_extracted_' + extract_datetime + '.csv'

    # Drop duplicates (if any)
    tweets_df.drop_duplicates(inplace=True)

    # Export dataframe as csv file with above filename
    tweets_df.to_csv(filename, index=False)
    print("writting the data into local file.....done")