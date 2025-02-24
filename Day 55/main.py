from flask import Flask

app = Flask(__name__)


def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper
def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper
def make_emphasize(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


@app.route('/')
def hello():
    return 'hello'

@app.route('/bye')
@make_underline
@make_bold
@make_emphasize
def bye():
    return 'bye!'

@app.route('/username/<name>/<int:number>')
def username(name, number):
    return f"Hello {name}! You are {number} years old."

if __name__ == '__main__':
    app.run(debug=True)
