#!/usr/bin/python3
"""
this will Use reddit's API
"""


import requests
after = None


def recurse(subreddit, hot_list=[]):
    """will be returning top ten post titles"""
    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    while results.status_code == 200:
        after_data = results.json().get("data").get("after")
        while after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
