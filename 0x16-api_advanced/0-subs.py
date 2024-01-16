#!/usr/bin/python3
"""
module queries info from the reddit API
"""
import requests
import sys


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    elif response.status_code == 404:
        return 0
    else:
        print(f"Error: {response.status_code}")
        return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <subreddit_name>")
        sys.exit(1)

    subreddit_name = sys.argv[1]
    subscribers_count = number_of_subscribers(subreddit_name)
    print(f"The number of subscribers in r/{subreddit_name} is: {subscribers_count}")
