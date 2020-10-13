# TQM - Task Queue Manager

---

This is a simple task queue written with Flask to count the number of words at a provided exisitng url.
It uses a [Python-RQ](https://python-rq.org/docs/workers/) worker that runs in the background wating for work to be processed and read jobs from the queues (in an endless loop till all jobs are done) when new tasks are added in there.

In general a Python worker exists solely as a work horse to perform lengthy or blocking tasks that we don’t want to perform inside web processes.

---

### Run the API

---

Start the API and Redis

```bash
docker-compose up
```

Open a new tab or terminal window and start the worker

```
rq worker
```

this will allow to watch all the jobs being performed in background from the worker.

Api is available [Here](http://localhost:8080/)

---

### Play with the API

---

1. Once all the services (API, worker and redis) are up and running go to [Add Tasks](http://localhost:8080/add-task)
   and submit an URL.

2. Refresh the page as many time as you want to simulate the adding tasks to the queue --> The number of queued jobs will increase straight away.

3. In a new tab open [Jobs](http://localhost:8080/jobs) to check the remaining queued jobs running in background. Refresh to update the number of queued tasks.

---

### Env variables

---

```bash
export FLASK_APP=api/wsgi.py
export FLASK_DEBUG=1
export FLASK_ENV=development
export APP_SETTINGS=Development
export REDIS_HOST=redis
export REDIS_PORT=6379
export REDIS_DB=0
```

---

RQ workers should run in process mangers like [systemd](https://python-rq.org/patterns/systemd/) in production environments.
