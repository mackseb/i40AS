from app import app
import zmq
from flask import Flask, render_template
import threading
from app import frontend

global task_id
task_id = 0


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/apps/reverse/<string:task>')
def reverse(task):
    global task_id
    task_id += 1
    thread_client = threading.Thread(target=frontend.main, args=(task_id, "reverse", task))
    thread_client.start()

    return render_template("reverse.html", task_id = task_id, task =task)
