#/usr/bin/env 
# ytHaikuBot.py

import praw
import configparser

def get_posts(reddit):
    yt_haiku = reddit.subreddit('youtubehaiku')
    for submission in yt_haiku.top(limit=100):
        print(submission.score, submission.title)

def main():
    config = configparser.ConfigParser()
    config.read('credentials.ini')
    redditCreds = config['Auth-Reddit']
    redditAPI = praw.Reddit(client_id=redditCreds['client_id'],
                         client_secret=redditCreds['client_secret'],
                         password=redditCreds['password'],
                         user_agent=redditCreds['user_agent'],
                         username=redditCreds['username'])
    get_posts(redditAPI)


if __name__ == '__main__':
    import os, sys
    main()
