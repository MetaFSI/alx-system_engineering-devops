#!/usr/bin/python3
""" Script that uses JSONPlaceholder API get informations about employee """
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    url = 'https://jsonplaceholder.typicode.com/'

    user_id = sys.argv[1]

    user_response = requests.get(url + 'users/{}'.format(user_id))
    user_info = user_response.json()
    user_name = user_info.get('name')

    todos_response = requests.get(url + 'todos', params={'userId': user_id})
    todos = todos_response.json()

    total_tasks = len(todos)
    completed_tasks = [task for task in todos if task.get('completed')]
    num_completed_tasks = len(completed_tasks)

    print("Employee {} is done with tasks ({}/{}):".format(user_name, num_completed_tasks, total_tasks))
    
    for task in todos:
        task_title = task.get('title')
        task_status = "X" if task.get('completed') else " "
        print("\t {} [{}]".format(task_title, task_status))
