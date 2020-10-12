#!/usr/bin/env python3
from flask import Blueprint, g, request, current_app as app

from api.tasks.handler import add_new_task

tasks = Blueprint("tasks", __name__)


@tasks.route('/')
def welcome():
    return 'Welcome to the queue task system!'


@tasks.route("/add-task", methods=["GET", "POST"])
def add_task():
    app.logger.info(f'[TASKS] {g.transaction_id}: got new request to add task')
    url = None

    if request.args:

        url = request.args.get("url")

    return add_new_task(url)
