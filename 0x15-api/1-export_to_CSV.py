#!/usr/bin/python3
import csv
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    user_id = int(sys.argv[1])
    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response_user = requests.get(url_user)
    if response_user.status_code != 200:
        print("User with ID {} doesn't exist".format(user_id))
        sys.exit(1)

    url_todo = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)
    response_todo = requests.get(url_todo)
    if response_todo.status_code != 200:
        print("Couldn't get TODO list for user with ID {}".format(user_id))
        sys.exit(1)

    employee_name = response_user.json().get('name')
    todo_list = response_todo.json()

    # Get the number of completed tasks
    num_completed_tasks = len([task for task in todo_list if task.get('completed')])

    # Create the CSV file
    filename = '{}.csv'.format(user_id)
    with open(filename, mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        for task in todo_list:
            writer.writerow([user_id, employee_name, task.get('completed'), task.get('title')])

    # Display the TODO list progress
    num_total_tasks = len(todo_list)
    print("Employee {} is done with tasks({}/{}):".format(employee_name, num_completed_tasks, num_total_tasks))
    for task in todo_list:
        if task.get('completed'):
            print("\t {}".format(task.get('title')))
