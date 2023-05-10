#!/usr/bin/python3

import requests
def count_words(subreddit, word_list):
    # Set the User-Agent header to avoid getting Too Many Requests errors.
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}

    # Make a request to the Reddit API.
    response = requests.get('https://api.reddit.com/r/' + subreddit + '/hot', headers=headers)

    # Check the response status code.
    if response.status_code == 200:
        # The request was successful.
        data = response.json()
        hot_list = []
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        count_dict = {}
        for word in word_list:
            word = word.lower()
            count = 0
            for title in hot_list:
                title = title.lower()
                if word in title:
                    count += 1
            count_dict[word] = count
        sorted_count_dict = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_count_dict:
            print(word, count)
    else:
        # The request failed.
        print(None)
