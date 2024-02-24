from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db
from datetime import datetime
from flask_wtf.csrf import CSRFProtect
from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


def __repr__(self):
    return f'User({self.username}, {self.email})'


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),
                                                                     EqualTo('password')])


def __repr__(self):
    return f'User({self.username}, {self.email})'


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


def init_db():
    db.create_all()
    print('OK')


def add_user(user: User):
    # user = User(username='john', email='john@example.com')
    db.session.add(user)
    db.session.commit()
    # print('John add in DB!')


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        new_user = User(username=name, email=email, password=password)
        init_db()
        add_user(new_user)
        return render_template('welcome.html', context=name, form=form)
    return render_template('register.html', form=form)


@app.route('/showbase/', methods=['GET', 'POST'])
def showbase():
    users = User.query.all()
    context = {'users': users}
    return render_template('showbase.html', **context)

@app.route('/forward/', methods=['GET', 'POST'])
def show():
    print('Показываю базу')
    users = User.query.all()
    context = {'users': users}
    return render_template('showbase.html',  **context)


if __name__ == '__main__':
    app.run(debug=True)
