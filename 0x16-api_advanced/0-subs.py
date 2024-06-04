#!/usr/bin/python3
""" this function to query subscribers."""
import requests


def number_of_subscribers(subreddit):
    """will return the total number of subscribers ."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    while response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
