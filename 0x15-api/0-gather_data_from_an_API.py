#!/usr/bin/python3
""" Script that uses JSONPlaceholder API get informations about employee """
import requests
import sys
import csv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user_id = sys.argv[1]
    user_url = '{}users/{}'.format(url, user_id)
    res = requests.get(user_url)
    user_info = res.json()
    
    todos_url = '{}todos?userId={}'.format(url, user_id)
    res = requests.get(todos_url)
    tasks = res.json()

    user_name = user_info.get('username')

    csv_filename = '{}.csv'.format(user_id)

    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:
            task_completed = "True" if task.get('completed') else "False"
            task_title = task.get('title')
            csv_writer.writerow([user_id, user_name, task_completed, task_title])

    print("CSV file '{}' has been created successfully.".format(csv_filename))
