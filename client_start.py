import zmq
from flask import Flask, jsonify, request, render_template
from structure import configuration_shell, structure_module
import json


app = Flask(__name__)
shell_client = structure_module.entity('client',configuration_shell.data)



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/apis', methods=['GET','POST'])
def apis():
    if request.method == 'POST':
        if request.form:
            postjson = request.form['JSON']
            postjson = json.loads(postjson)
            api_name = postjson['api_name']
            api_data = postjson['api_data']

            if configuration_shell.data.get(api_name, False):

                MESSAGE = shell_client.create_message(TO = configuration_shell.data[api_name]['identity'], CORE_pyobj = api_data)
                shell_client.send(MESSAGE)
                MESSAGE = shell_client.receive()

                return jsonify(shell_client.extract_core(MESSAGE))

            else:

                response = {'response' : 'unknown api'}

                return jsonify(response)



        if request.json:
            postjson = request.get_json()
            api_name = postjson['api_name']
            api_data = postjson['api_data']

            if configuration_shell.data.get(api_name, False):

                MESSAGE = shell_client.create_message(TO = configuration_shell.data[api_name]['identity'], CORE_pyobj = api_data)
                shell_client.send(MESSAGE)
                MESSAGE = shell_client.receive()

                return jsonify(shell_client.extract_core(MESSAGE))

            else:

                response = {'response' : 'unknown api'}

                return jsonify(response)
    else:
        return render_template('api_request.html')








if __name__ == "__main__":
    app.run(host='0.0.0.0')
