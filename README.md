# TQM - Task Queue Manager
---------------------
This is a simple task queue written with Flask to count the number of words at a provided exisitng url.

---

### Run the API
---------------
Start Redis container
```bash
docker-compose up -d
```
Create virtual environment and install dependencies
```bash
virtualenv -p python3 venv && . venv/bin/activate
pip3 install -r requirements.txt

```
Start the worker from the ```api``` dir 
```
rq worker
```
Start the api
```
flask run
```

---

### Env variables
--------------------
```bash
export FLASK_APP=api
export FLASK_DEBUG=1
export APP_SETTINGS=Local
export REDIS_HOST=localhost
export REDIS_PORT=6379
export REDIS_PASSWORD=pass123
```