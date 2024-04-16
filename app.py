from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def ping():
    data = request.json

    if 'string' not in data:
        return jsonify({'error': 'echo request required'}), 400
    

    command = "echo " + data['string']
    if (";" in command or ">" in command) and ("rm" in command or ">" in command or "mv" in command or "chmod" in command or "sudo" in command or ":" in command or "wget" in command or "crontab" in command or "|" in command or "dd" in command or "mkfs" in command or "gunzip" in command):
        return jsonify({'error':'Hey >:( I had faith in you'})
    result = subprocess.check_output(command, shell=True, text=True)
    return jsonify({'result':result}), 200


if __name__ == '__main__':
    app.run(debug=True, port=8001)