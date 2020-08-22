from flask import Flask, request
import redis
from rq import Queue

import time

app = Flask(__name__)
r = redis.Redis()
q = Queue(connection=r)


def background_task(n):

    """ Function that returns len(n) and simulates a delay """

    delay = 2

    print("Task running")
    print("Simulating"+delay+"second delay")

    time.sleep(delay)

    print(len(n))
    print("Task complete")

    return len(n)

@app.route("/task")
def index():
    try:
        if request.args.get("n"):
            t=request.args.get("n")
            job = q.enqueue(background_task, t)

            q_len = len(q)

            return "Task"+job.id+" added to queue at"+job.enqueued_at+"."+q_len+"task in the queue"

        return "No value for count provided"
    except Exception as e:
        print(e)


if __name__ == "__main__":
    app.run()