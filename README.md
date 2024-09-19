# A simple Flask skeleton with docker

A simple flask skeleton with templating and optional route powered by docker

## From 0 to a __simple__ Docker image (on Debian/Ubuntu)

Install deps:

```bash
apt-get install docker docker-compose-v2 python3 python3-venv
```

Create project dir:

```bash
mkdir flask-docker
cd flask-docker
python3 -m venv .venv
. .venv/bin/activate
pip install Flask
pip freeze > requirements.txt
```

Create app.py in project root:

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

Create Dockerfile:

```
FROM python:3

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
```

## Build and run image

```
docker build --tag flask-docker .
docker run -d -p 5000:5000 flask-docker
```

Open http://127.0.0.1:5000
