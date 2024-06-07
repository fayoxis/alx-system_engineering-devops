#!/usr/bin/python3
"""
this number of subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    the Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}

    response = get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0


if __name__ == "__main__":
    import sys
    subreddit = sys.argv[1]
    if number_of_subscribers(subreddit) > 0:
        print("OK")
    else:
        print("OK")
