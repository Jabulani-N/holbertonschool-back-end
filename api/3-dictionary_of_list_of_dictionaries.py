#!/usr/bin/python3
"""returns information about emplopyee todo list progress"""
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


if __name__ == '__main__':
    gather_data()
