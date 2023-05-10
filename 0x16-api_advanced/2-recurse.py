#!/usr/bin/python3

import requests
def recurse(subreddit, hot_list=[]):
    # Set the User-Agent header to avoid getting Too Many Requests errors.
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}

    # Make a request to the Reddit API.
    response = requests.get('https://api.reddit.com/r/' + subreddit + '/hot', headers=headers)

    # Check the response status code.
    if response.status_code == 200:
        # The request was successful.
        data = response.json()
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        next_page = data['data']['after']
        if next_page:
            recurse(subreddit, hot_list, next_page)
        return hot_list
    else:
        # The request failed.
        return None
