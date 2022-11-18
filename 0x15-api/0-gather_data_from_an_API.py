#!/usr/bin/python3
"""
Make a request from the API: Return the TODO list progress given employee ID
"""

import requests
from sys import argv

def information():
    """return the datas from the API"""
    users = requests.get("http://jsonplaceholder.typicode.com/users")
    for user in users.json():
        if user.get('id') == int(argv[1]):
            EMPLOYEE_NAME = (user.get('name'))
            break
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for todo in todos.json():
        if todo.get('userId') == int(argv[1]):
            TOTAL_NUM_OF_TASKS += 1
            if todo.get('completed') is True:
                    NUMBER_OF_DONE_TASKS += 1
                    TASK_TITLE.append(t.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUM_OF_TASKS))
    for task in TASK_TITLE:
        print("\t {}".format(task))


if __name__ == "__main__":
    information()
