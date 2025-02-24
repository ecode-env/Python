from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello'


@app.route('/bye')
def bye():
    return 'bye!'


@app.route('/username/<name>/<int:number>')
def username(name, number):
    return f"hello {name}! you are {number} years old"


if __name__ == '__main__':
    app.run(debug=True)
