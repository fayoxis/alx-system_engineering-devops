#!/usr/bin/python3
""" the Module that consumes the Reddit API and returns a list
articles."""
import requests


def recurse(subreddit, hot_list=[], n=0, after=None):
    """ this queries the API and returns a list containing the titles of
    all articles
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'custom'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    while r.status_code == 200:
        r = r.json()
        for post in r.get('data').get('children'):
            hot_list.append(post.get('data').get('title'))
        while r.get('data').get('after'):
            recurse(subreddit, hot_list)
        return hot_list
    else:
        return None
