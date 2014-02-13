#coding=utf8

from flask import Flask
#from blog.database import db_session

app = Flask(__name__)
#app.config.from_object('config')
app.debug = True

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
    app.run(host='0.0.0.0', port=5000)
