from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

# Note: the connection string after :// contains the following info:
# user:password@server:portNumber/databaseName

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://get-it-done:beproductive@localhost:8889/get-it-done'

app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    app.run()