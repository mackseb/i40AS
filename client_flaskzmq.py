import zmq
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/<string:api_name>')
def api(api_name):
    return render_template("api.html", api_name =api_name)




if __name__ == "__main__":
    app.run()
