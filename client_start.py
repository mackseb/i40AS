import zmq
from flask import Flask, jsonify, request, render_template
from structure import configuration_shell, structure_client



app = Flask(__name__)
shell_client = structure_client.entity(configuration_shell.data)



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/<string:api_name>', methods=['POST'])
def api(api_name):


    if configuration_shell.data.get(api_name, False):

        MESSAGE = shell_client.create_message(TO = configuration_shell.data[api_name]['identity'], CORE_pyobj = request.get_json())
        shell_client.send(MESSAGE)
        MESSAGE = shell_client.receive()

        return jsonify(shell_client.extract_core(MESSAGE))

    else:

        response = {'response' : 'unknown api'}

        return jsonify(response)





if __name__ == "__main__":
    app.run()
