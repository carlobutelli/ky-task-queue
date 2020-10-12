#!/usr/bin/env python3
from api import q
from .utils import count_words

from flask import render_template


def add_new_task(url: str):

    jobs = q.jobs  # Get jobs in the queue

    message = None

    if url:
        # Send task to the queue
        task = q.enqueue(count_words, url)

        # Get list of updated jobs in the queue
        jobs = q.jobs

        q_len = len(q)  # Get the queue length

        message = f"Task queued at {task.enqueued_at.strftime('%a, %d %b %Y %H:%M:%S')}. {q_len} jobs queued"

    return render_template("add_task.html", message=message, jobs=jobs)


def get_remaining_jobs():
    jobs = q.jobs
    q_len = len(q)
    message = f"Remaining {q_len} jobs queued"
    return render_template("show_queued_jobs.html", message=message, jobs=jobs)
