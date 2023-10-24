from flask import Flask, render_template

app = Flask(__name__)

# Пример данных о студентах (замените на свои данные)
students = [
    {"Имя": "Иван", "Фамилия": "Иванов", "Возраст": 20, "Средний балл": 4.5},
    {"Имя": "Петр", "Фамилия": "Петров", "Возраст": 22, "Средний балл": 3.8},
    {"Имя": "Мария", "Фамилия": "Сидорова", "Возраст": 21, "Средний балл": 4.0},
]

@app.route('/')
def students_table():
    return render_template('students.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
