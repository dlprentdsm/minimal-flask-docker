import redis
from flask import Flask

app = Flask(__name__)
REDIS = redis.Redis(host='redis', port=6379)


def get_visit_count():
    try:
        return REDIS.incr('hits')
    except redis.exceptions.ConnectionError as exc:
        raise exc


@app.route('/')
def hello_world():
    visits = get_visit_count()
    return '<html><body><h1>Minimal Flask Example</h1>This page has been visited {} times.</body></html>'.format(visits)
