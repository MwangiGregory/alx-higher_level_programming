#!/usr/bin/python3
"""This script returns information about
an employees TODO list progress"""
import sys
import requests

if __name__ == "__main__":

    r = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={sys.argv[1]}'
    )
    tasks = r.json()
    completed = 0
    employee_name = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    ).json().get('name')
    for task in tasks:
        if task.get('completed'):
            completed = completed + 1
    print(f'Employee {employee_name} is done with tasks', end='')
    print(f'({completed}/{len(tasks)}):')

    for task in tasks:
        print(f'\t {task.get("title")}')
