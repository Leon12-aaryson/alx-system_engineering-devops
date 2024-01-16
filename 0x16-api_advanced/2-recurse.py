#!/usr/bin/python3
import requests
import sys


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'Custom User Agent'}

    if after:
        url += f"&after={after}"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if not posts:
            return hot_list
        else:
            hot_list.extend([post['data']['title'] for post in posts])
            return recurse(subreddit, hot_list, after=data['data']['after'])
    elif response.status_code == 404:
        return None
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <subreddit_name>")
        sys.exit(1)

    subreddit_name = sys.argv[1]
    result = recurse(subreddit_name)

    if result is not None:
        for title in result:
            print(title)
    else:
        print(f"Invalid subreddit: {subreddit_name}")
