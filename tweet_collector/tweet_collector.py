import time
from datetime import datetime, timedelta, timezone, tzinfo
import logging
import pytz
import pymongo
import tweepy
import credentials
import random

# Set timezone to UTC 
tz = pytz.timezone('UTC') 

##################
# Authentication #
##################

#Import BEARER_TOKEN from a separate credentials file.
BEARER_TOKEN = credentials.Bearer_Token

tweet_client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    wait_on_rate_limit=True,
    )

##################
#Move to MongoDB #
##################

while True:

    # Create a connection to the MongoDB database server
    client = pymongo.MongoClient(host='mongodb') # hostname = servicename for docker-compose pipeline

    # Create/use a database(equivalent of CREATE DATABASE twitter)
    db = client.twitter    

    # Define the collection (equivalent of CREATE TABLE tweets)
    collection = db.tweets     

    ########################
    # Get Twitter Queries  #
    ########################

    while True:
    # Set the timeinterval within which to search for tweets.
    # Default is 5 mins. When changing, adapt it in every part of the pipeline.
        time_now = datetime.now(tz)
        end_time = time_now - timedelta(seconds=10)
        start_time = end_time - timedelta(minutes=310)
        break
    
    # You can enter your search query here. Default is: berlin
    search_query = "berlin -is:retweet -is:reply -is:quote lang:en -has:links"

    # Get specific parts of tweets within given timeinterval. Default max = 1000.
    cursor = tweepy.Paginator(
            method=tweet_client.search_recent_tweets,
            query=search_query,
            end_time=end_time,
            start_time=start_time,
            tweet_fields=['author_id', 'created_at', 'public_metrics'],
    ).flatten(limit=1000)

    # Insert the tweets into MongoDB collection.
    for tweet in cursor:    
        logging.warning('-----Tweet being written into MongoDB-----')
        logging.warning(tweet)
        collection.insert_one(dict(tweet))
        logging.warning(str(datetime.now()))
        logging.warning('----------\n')

    time.sleep(300)