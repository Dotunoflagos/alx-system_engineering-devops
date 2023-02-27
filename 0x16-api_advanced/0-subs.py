#!/usr/bin/python3
"""
queries the Reddit API 
"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API"""
    headers = {
        "User-Agent": "0x16. API_advanced-e"
        }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    sub = response.json().get("data").get("subscribers")
    return sub
