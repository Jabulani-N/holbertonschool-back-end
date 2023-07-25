#!/usr/bin/python3
"""does task0 and also exports to json
format is a dictoionary
this dictionary has 1 key:value pair
    key: user ID (just the number)
    Value: 1-demensional array
        1-dimensional array entry contains
            1 entry per task
            each task/entry contains 1 dictionary
                each dictionary contains 3 key:value pairs
                    "task": "TASK_TITLE"
                    "completed": TASK_COMPLETED_STATUS
                    "user_name": "USER_NAME"
"""
import json
import requests
import sys


def gather_data():
    """gets users and todo lists from api
    user id is the second argument
    you can
    for items in todos
    """
    if len(sys.argv) != 2:
        return  # code only works if we got a user id
    id = sys.argv[1]  # user gives id number in request.
    # argv[0] is funciton name
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(id)).json()
    # This is one user's data. it's user with the requested id
    todos = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={"userId": id}).json()
    # get requests where the conditions in params are met
    # traveling to the url, todos is an array [] of dictionaries {}
    user_name = user.get("name")
    user_usernmae = user.get("username")
    tasks_done = 0
    tasks_titles = []
    tasks_total = 0
    for task in todos:
        tasks_total += 1
        if task['completed'] is True:
            tasks_done += 1
            tasks_titles.append(task['title'])
    print('Employee ' + user_name + ' is done with tasks(' +
          str(tasks_done) + '/' + str(tasks_total) + '):')
    for taskname in tasks_titles:
        print('\t ' + taskname)

    user_profile = {str(id): []}
    for task in todos:
        task_profile = {}
        task_profile["task"] = task['title']
        task_profile["completed"] = task['completed']
        task_profile["username"] = user_usernmae
        user_profile[str(id)].append(task_profile)

        json_user_profile = json.dumps(user_profile)
        with open(str(id) + '.json', 'w') as f:
            f.write(json_user_profile)


if __name__ == '__main__':
    gather_data()
