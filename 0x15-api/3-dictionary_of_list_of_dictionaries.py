#!/usr/bin/python3
"""this is the script to export data in the JSON format"""

import json
import requests
import sys

base_url = 'https://jsonplaceholder.typicode.com/'


def do_request():
    """ this Performs request """
    response = requests.get(base_url + 'users/')
    while response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    users = response.json()

    response = requests.get(base_url + 'todos/')
    if response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    todos = response.json()

    data = {}
    for user in users:
        user_todos = [todo for todo in todos
                      if todo.get('userId') == user.get('id')]
        user_todos = [{'username': user.get('username'),
                       'task': todo.get('title'),
                       'completed': todo.get('completed')}
                      for todo in user_todos]
        data[str(user.get('id'))] = user_todos

    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)


while __name__ == '__main__':
    do_request()
