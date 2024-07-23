#!/usr/bin/python3
'''
    This module contains the function top_ten
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''
        Returns the top ten posts for a given subreddit
    '''
    user_agent = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    try:
        response = requests.get(url, headers=user_agent)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
    except KeyError:
        print("Subreddit not found or unable to fetch data.")

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 script_name.py subreddit_name")
        exit(1)
    subreddit_name = argv[1]
    top_ten(subreddit_name)