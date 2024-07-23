#!/usr/bin/python3
'''
    This module contains the function number_of_subscribers
'''


import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''
        Returns the number of subscribers for a given subreddit
    '''
    user_agent = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        response = requests.get(url, headers=user_agent)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return 0
    except KeyError:
        print("Subreddit not found or unable to fetch data.")
        return 0


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 script_name.py subreddit_name")
        exit(1)
    subreddit_name = argv[1]
    subscriber_count = number_of_subscribers(subreddit_name)
    print(subscriber_count)