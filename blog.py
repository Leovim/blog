#coding=utf8
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello/<name>')
def hello(name):
    return 'Hello ' + name + '!'

@app.route('/test')
def test():
    return '正在測試.'

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', 5000)
