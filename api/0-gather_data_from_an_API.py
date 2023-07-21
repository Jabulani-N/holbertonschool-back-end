#!/usr/bin/python3
"""remmber the shebang

Write a Python script that,
using this REST API,
for a given employee ID (input argument),
returns information about their todo list progress
"""
from flask import Flask
import requests, sys
app = Flask(__name__)

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
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'\
                              .format(id)).json()
    # This is one user's data. it's user with the requested id
    todos = requests.get('https://jsonplaceholder.typicode.com/todos',\
                          params={"userId": id}).json()
    # get requests where the conditions in params are met
    username = user.get("name")


if __name__ == '__main__':
    gather_data()
