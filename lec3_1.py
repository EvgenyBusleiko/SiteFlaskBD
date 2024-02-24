from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm 

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqllite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'




if __name__=='__main__':
    app.run(debug=True)