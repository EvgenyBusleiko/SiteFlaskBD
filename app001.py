from flask import Flask, render_template, flash
from models import db, Student, Faculty
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = b'8fda4c95f8ced93390919e911abb6b9dcd317ac21a6662e23748d47345e1cb72'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

db.init_app(app)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')


@app.cli.command('fill-t1')
def fill_task1_tables():
    # for i in range(1, 6):
    #     new_faculty = Faculty(name=f"Faculty_{i}")
    #     db.session.add(new_faculty)
    # db.session.commit()

    for i in range(1, 11):
        new_student = Student(
            first_name=f'First_name{i}',
            last_name=f'Last_name{i}',
            age=random.randint(10, 90),
            gender=random.choice([True, False]),
            group=random.randint(100, 200),
            faculty_id=random.randint(1, 5)
        )
        db.session.add(new_student)
    db.session.commit()
    print("ok")


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


def result(message):
    return render_template('result.html', message=message)


# Создать базу данных для хранения информации о студентах университета.
# База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их факультета.
@app.route('/task1/')
def task1_index():
    students = Student.query.all()
    return render_template('task1/index.html', students=students, title="task1")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=True)