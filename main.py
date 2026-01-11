from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user/<name>')
def user_greeting(name):
    return f'Hello, {name}! Welcome to Flask!'


if __name__ == '__main__':
    app.run(debug=True)
