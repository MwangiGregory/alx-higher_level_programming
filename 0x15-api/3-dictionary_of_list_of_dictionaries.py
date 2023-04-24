#!/usr/bin/python3
"""This  Python script to export data in the JSON format"""
import sys
import json
import requests

if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    temp = {}
    for user in users:
        userId = user.get('id')
        tasks = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={userId}')
        tasks = tasks.json()
        temp_list = []
        for task in tasks:
            temp_dict = {}
            temp_dict["username"] = user.get("username")
            temp_dict["completed"] = task.get("completed")
            temp_dict["task"] = task.get("title")
            temp_list.append(temp_dict)
        temp[userId] = temp_list

    with open('todo_all_employees.json', 'w', encoding='utf8') as f:
        json.dump(temp, f)
