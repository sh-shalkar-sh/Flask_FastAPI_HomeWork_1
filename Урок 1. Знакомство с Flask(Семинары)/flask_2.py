from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Main page'

@app.route('/about/')
def about():
    return 'About'


@app.route('/contact/')
def contact():
    return 'Contact'


if __name__ == '__main__':
    app.run(debug=True)