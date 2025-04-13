from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Khurana ECS Container."

@app.route('/host')
def hostname():
    return f"Hostname: {socket.gethostname()}"

@app.route('/ip')
def ip():
    return f"Internal IP: {socket.gethostbyname(socket.gethostname())}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
