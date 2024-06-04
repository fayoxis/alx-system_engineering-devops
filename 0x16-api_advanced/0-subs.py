#!/usr/bin/python3
""" 0x16. API advanced, task 0. How many subs?
"""
from requests import get


def number_of_subscribers(subreddit):
    """ Queries Reddit API and returns number of subscribers (not active users)
    for a given subreddit.

    Args:
        subreddit (str): subreddit to query

    Return:
        number of current subscribers to `subreddit`, or 0 if `subreddit` is
    invalid
    """
    response = get('https://www.reddit.com/r/{}/about.json'.format(subreddit),
                   headers={'User-Agent': 'allelomorph-app0'})
    # non-existent subreddits sometimes return 404
    if response.status_code != 200:
        return 0
    # and sometimes return a dummy JSON dict with only 'Listing' key
    return response.json().get('data').get('subscribers', 0)
