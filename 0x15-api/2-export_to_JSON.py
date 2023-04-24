#!/usr/bin/python3
"""This  Python script to export data in the JSON format"""
import sys
import json
import requests

if __name__ == "__main__":
    user_id = sys.argv[1]
    r = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    )
    tasks = r.json()
    completed = 0
    employee_name = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    ).json().get('name')
    temp = {}
    temp[user_id] = []
    for task in tasks:
        temp_dict = {}
        temp_dict["task"] = task.get('title')
        temp_dict["completed"] = task.get("completed")
        temp_dict["username"] = employee_name
        temp[user_id].append(temp_dict)

    with open(f'{user_id}.json', 'w', encoding='utf8') as f:
        json.dump(temp, f)
