#!/usr/bin/python3
"""
print titles
"""
import requests
import sys


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    elif response.status_code == 404:
        print(None)
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <subreddit_name>")
        sys.exit(1)

    subreddit_name = sys.argv[1]
    # print(f"Top 10 posts in r/{subreddit_name}:")
    top_ten(subreddit_name)
