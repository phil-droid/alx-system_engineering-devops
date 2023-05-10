import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/users')
users = json.loads(response.text)

todo_dict = {}
for user in users:
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={user["id"]}')
    todos = json.loads(response.text)
    todo_list = []
    for todo in todos:
        todo_list.append({"username": user["username"], "task": todo["title"], "completed": todo["completed"]})
    todo_dict[user["id"]] = todo_list

with open("todo_all_employees.json", "w") as f:
    json.dump(todo_dict, f)
