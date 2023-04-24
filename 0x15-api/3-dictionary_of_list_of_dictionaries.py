#!/usr/bin/python3
"""This  Python script to export data in the JSON format"""
import sys
import json
import requests

if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    temp = {}
    for user in users:
        temp[user.get('id')] = []
        tasks = requests.get(
            f'https://jsonplaceholder.typicode.com/todos? \
                userId={user.get("id")}').json()
        # print(type(tasks))
        for task in tasks:
            temp_dict = {}
            temp_dict["username"] = user.get("username")
            temp_dict["task"] = task.get("title")
            temp_dict["completed"] = task.get("completed")
            temp[user.get('id')].append(temp_dict)

    with open('todo_all_employees.json', 'w', encoding='utf8') as f:
        json.dump(temp, f)
