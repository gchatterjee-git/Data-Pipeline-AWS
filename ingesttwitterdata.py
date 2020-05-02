# -*- coding: utf-8 -*-
"""
Created on Fri May  1 19:43:36 2020

@author: Gaurav
"""

import tweepy
import boto3
import json
import time
import twittercred


topic = 'COVID'

if __name__ == '__main__':

    client = boto3.client('firehose')
    start_time = time.time()
    timeDiff = 0
    tweets = []
    while True:
        tweets = tweepy.Cursor(api.search, q=topic).items(1000)
        for tweet in tweets:
            response = client.put_record(
                DeliveryStreamName='kinesisgaurav',
                Record={
                    'Data': json.dumps(tweet._json) + '\n'
                }


            )
            print("Collecting Tweets....")
            print(response)
            
            #time.sleep(60)
            #response = client.delete.resouce('kinesisgaurav')
