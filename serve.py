from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/',methods = ['POST'])
def run_stress_cpu():
    subprocess.Popen(["python3","stress_cpu.py"])
    return "success"

@app.route('/',methods = ['GET'])
def get_hostname():
    return socket.gethostname()

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000)

