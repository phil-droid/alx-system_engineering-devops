#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import requests
import sys


if __name__ == '__main__':
    # Fetching user id from command line argument
    user_id = sys.argv[1]

    # URL endpoint to fetch user information
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    # URL endpoint to fetch user's TODO information
    todos_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)

    # GET request to fetch user information
    user_res = requests.get(user_url)
    user_data = user_res.json()

    # GET request to fetch user's TODO information
    todos_res = requests.get(todos_url)
    todos_data = todos_res.json()

    # Total number of tasks
    total_tasks = len(todos_data)

    # Number of completed tasks
    completed_tasks = 0
    completed_tasks_list = []
    for task in todos_data:
        if task.get('completed') is True:
            completed_tasks += 1
            completed_tasks_list.append(task.get('title'))

    # Displaying the result
    print("Employee {} is done with tasks({}/{}):".format(user_data.get('name'), completed_tasks, total_tasks))
    for task in completed_tasks_list:
        print("\t {}".format(task))
