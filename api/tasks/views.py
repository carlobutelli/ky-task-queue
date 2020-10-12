#!/usr/bin/env python3
from flask import Blueprint


task = Blueprint("tasks", __name__)


@task.route('/')
def welcome():
    return 'Welcome to the queue task system!'
