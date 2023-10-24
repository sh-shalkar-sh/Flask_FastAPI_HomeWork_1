from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/<name>/')
def hello(name='незнокомец'):
    return f'Привет, {name.capitalize()}!'


@app.route('/file/<path:file>')
def set_path(file):
    print(type(file))
    return f'Путь до файлы "{file}"'


@app.route('/number/<float:num>/')
def set_number(num):
    print(type(num))
    return f'Передано число {num}'


if __name__ == '__main__':
    app.run(debug=True)