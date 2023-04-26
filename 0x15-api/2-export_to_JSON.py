import json
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: {} USER_ID".format(sys.argv[0]))
    sys.exit(1)

USER_ID = sys.argv[1]
URL = "https://jsonplaceholder.typicode.com/todos?userId={}".format(USER_ID)

response = requests.get(URL)

if response.status_code != 200:
    print("Error fetching data from API: Status code {}".format(response.status_code))
    sys.exit(1)

data = response.json()

tasks = []
for item in data:
    task = {
        "task": item["title"],
        "completed": item["completed"],
        "username": ""
    }
    tasks.append(task)

if len(tasks) > 0:
    URL = "https://jsonplaceholder.typicode.com/users/{}".format(USER_ID)
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        username = data["username"]
        for task in tasks:
            task["username"] = username

json_data = {USER_ID: tasks}
with open("{}.json".format(USER_ID), "w") as f:
    json.dump(json_data, f)
