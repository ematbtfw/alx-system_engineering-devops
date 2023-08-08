#!/usr/bin/python3
"""
Importing requests module
"""

from requests import get


def number_of_subscribers(subreddit):
    # Get the JSON response from the Reddit API.
    response = requests.get(
        f"https://api.reddit.com/r/{subreddit}/about", headers={"User-Agent": "my-app"}
    )
    # Check if the response was successful.
    if response.status_code != 200:
        return 0
    # Get the number of subscribers from the JSON response.
    response_json = response.json()
    return response_json["subscribers"]