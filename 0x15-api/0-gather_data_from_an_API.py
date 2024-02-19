#!/usr/bin/python3
""" Script uses JSONPlaceholder API to get information about an employee's tasks """

import requests
import sys

def get_employee_todo_progress(employee_id):
    url = 'https://jsonplaceholder.typicode.com/'

    # Fetch user details
    user_response = requests.get(f'{url}users/{employee_id}')
    if user_response.status_code != 200:
        print("Error: Unable to fetch employee details.")
        return

    user = user_response.json()

    # Fetch tasks for the user
    tasks_response = requests.get(f'{url}todos?userId={employee_id}')
    if tasks_response.status_code != 200:
        print("Error: Unable to fetch employee tasks.")
        return

    tasks = tasks_response.json()
    completed_tasks = [task for task in tasks if task.get('completed')]

    # Display employee's progress
    print(f"Employee {user.get('name')} is done with tasks ({len(completed_tasks)}/{len(tasks)}):")
    for task in completed_tasks:
        print(f"\t{task.get('title')}")

if __name__ == "__main__":
    # Check if an argument is provided
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Check if the provided argument is a valid integer
    if not employee_id.isdigit():
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
