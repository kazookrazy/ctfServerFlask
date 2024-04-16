from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/ping', methods=['POST'])
def ping():
    data = request.json

    if 'string' not in data:
        return jsonify({'error': 'echo request required'}), 400
    
    command = "echo " + data['string']
    result = subprocess.check_output(command, shell=True, text=True)
    return jsonify({'result':result}), 200


if __name__ == '__main__':
    app.run(debug=True, port=8001)