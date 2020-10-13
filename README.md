# TQM - Task Queue Manager

---

This is a simple task queue written with Flask to count the number of words at a provided exisitng url.
It uses a [Python-RQ](https://python-rq.org/docs/workers/) worker that runs in the background wating for work to be processed and read jobs from the queues (in an endless loop till all jobs are done) when new tasks are added in there.

In general a Python worker exists solely as a work horse to perform lengthy or blocking tasks that we don’t want to perform inside web processes.

---

### Run the API

---

Start Redis container

```bash
docker-compose up -d
```

Create virtual environment and install dependencies

```bash
virtualenv -p python3 venv && . venv/bin/activate
pip3 install -r requirements.txt

```

Start the worker

```
rq worker
```

Open a new tab or terminal window and start the api

```
. venv/bin/activate && flask run -p 8080
```

Api is available [Here](http://localhost:8080)

---

### Play with the API

---

1. Once the API is up and running with the worker and redis go to [Add Tasks](http://localhost:8080/add-task)
   and submit an URL.

2. Refresh the page as many time as you want to simulate to add tasks to the queue --> The number of queued jobs will increase straight away.

3. In a new tab open [Jobs](http://localhost:8080/jobs) to check the remaining queued jobs running in background. Refresh to update the number of queued tasks.

---

### Env variables

---

```bash
export FLASK_APP=api/wsgi.py
export FLASK_DEBUG=1
export APP_SETTINGS=Local
export REDIS_HOST=localhost
export REDIS_PORT=6379
export REDIS_PASSWORD=pass123
```

---

RQ workers should run in process mangers like [systemd](https://python-rq.org/patterns/systemd/) in production environments.
