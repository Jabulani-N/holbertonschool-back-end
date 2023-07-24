#!/usr/bin/python3
"""does task0 and also writes a csv file

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
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(id)).json()
    # This is one user's data. it's user with the requested id
    todos = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={"userId": id}).json()
    # get requests where the conditions in params are met
    # traveling to the url, todos looks to be an array [] of dictionaries {}
    user_name = user.get("name")
    user_username = user.get("username")

    task_compilation = []
    for task in todos:
        task_data = []
        task_data.append('' + str(task['userId']))
        task_data.append('' + user_username + '')
        task_data.append('' + str(task['completed']))
        task_data.append('' + task['title'] + '')
        task_compilation.append(task_data)
    with open(id + '.csv', 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(task_compilation)

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
