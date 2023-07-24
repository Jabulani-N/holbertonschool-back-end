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
        tasks_total += 1
        if task['completed'] is True:
            tasks_done += 1
            tasks_titles.append(task['title'])
    print('Employee ' + username + ' is done with tasks(' +
          str(tasks_done) + '/' + str(tasks_total) + '):')
    for taskname in tasks_titles:
        print('\t ' + taskname)
    with open('data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(VARIABLE HOLDING THE DATA TO WRITE.
                        CAN WRITE ARRAYS FILLED WITH STRINGS)


if __name__ == '__main__':
    gather_data()
