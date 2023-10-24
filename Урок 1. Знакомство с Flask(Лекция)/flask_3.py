from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/Фёдор/')
@app.route('/Fedor/')
@app.route('/Федя/')
def fedor():
    return 'Привет, Федор!'


if __name__ == '__main__':
    app.run(debug=True)
