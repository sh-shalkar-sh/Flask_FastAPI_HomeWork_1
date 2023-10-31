from flask import Flask, request, render_template, redirect, url_for, make_response

app = Flask(__name__)


# Главная страница с формой для ввода имени и электронной почты
@app.route('/')
def index():
    return render_template('index.html')


# Обработка данных формы и создание cookie-файла
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    # Создание cookie-файла
    response = make_response(redirect(url_for('welcome')))
    response.set_cookie('user_data', f'{name}::{email}')

    return response


# Страница приветствия, где отображается имя пользователя
@app.route('/welcome')
def welcome():
    user_data = request.cookies.get('user_data')
    if user_data:
        name, email = user_data.split('::')
        return render_template('welcome.html', name=name)
    else:
        return redirect(url_for('index'))


# Удаление cookie-файла и перенаправление на страницу ввода данных
@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('index')))
    response.delete_cookie('user_data')
    return response


if __name__ == '__main__':
    app.run(debug=True)
