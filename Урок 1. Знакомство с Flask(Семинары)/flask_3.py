from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Main page_2'

@app.get('/calc/<int:number_1>/<int:number_2>')
def set_number(number_1, number_2):
    return f'Сумма: {number_1 + number_2}'

@app.get('/len/<string:word>/')
def word_len(word):
    return f'Длина слов: {len(word)}'



if __name__ == '__main__':
    app.run(debug=True)