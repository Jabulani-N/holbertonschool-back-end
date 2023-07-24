#!/usr/bin/python3
"""returns information about emplopyee todo list progress

we're gonna use csv.writer and writerow to write the contents of an array
into a csv file
we're gonna do that in a for loop
for task in tasklist
"""
import csv
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
    # Arguments will always be string
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(id)).json()
    # This is one user's data. it's user with the requested id
    todos = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={"userId": id}).json()
    # get requests where the conditions in params are met
    # traveling to the url, todos looks to be an array [] of dictionaries {}
    username = user.get("name")
    tasks_done = 0
    tasks_titles = []
    tasks_total = 0
    for task in todos:
        if task['completed'] is True:
            tasks_titles.append(task['title'])

    task_compilation = []
    for task in todos:
        task_data = []
        task_data.append(task['userId'])
        task_data.append(username)
        task_data.append(task['completed'])
        task_data.append(task['title'])
        task_compilation.append(task_data)
    with open(id + '.csv', 'w') as f:
        writer = csv.writer(f)
        # writerows can handle 2-dimensional arrays
        # writerow excusively handles 1-dimensional arrays
        writer.writerows(task_compilation)


if __name__ == '__main__':
    gather_data()
