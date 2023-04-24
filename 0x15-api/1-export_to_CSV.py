#!/usr/bin/python3
"""Python script to export data in the CSV format
Format must be: "USER_ID","USERNAME",
"TASK_COMPLETED_STATUS","TASK_TITLE"""


if __name__ == "__main__":
    import sys
    import requests
    import csv

    r = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={sys.argv[1]}'
    )
    tasks = r.json()
    completed = 0
    username = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    ).json().get('name')

    with open(f'{sys.argv[1]}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in tasks:
            row = [sys.argv[1], username, task.get('completed'),
                   task.get('title')]
            writer.writerow(row)
