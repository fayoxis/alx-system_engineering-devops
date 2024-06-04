#!/usr/bin/python3
"""
this Script that queries subscribers on a given Reddit API.
"""


import requests


def number_of_subscribers(subreddit):
    """This will Return the total number of subscribers."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    while response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
