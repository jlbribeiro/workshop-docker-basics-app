#!/usr/bin/env python

import redis
from flask import Flask

app = Flask(__name__)
r = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route("/")
def hello():
    n_visits = r.incr('visits')
    return "Hello, visitor {0}!".format(n_visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
