from flask import Flask


app = Flask(__name__)



@app.route('/')
def index():
    return 'Main page_2'

html = '''<h1> Моя первая HTML страница </h1>
<p> Знакомство с Flask </p>
'''


@app.get('/html/')
def my_html():
    return html

if __name__ == '__main__':
    app.run(debug=True)