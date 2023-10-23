from flask import Flask, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_moment import Moment
from datetime import datetime

from flask import jsonify, flash, render_template, redirect, url_for
import requests

from wtforms import Form, StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf import FlaskForm
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
moment = Moment(app)

# Database with 4 columns: is, question, answer, created_at
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(300), nullable=False)
    answer = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.String(50))

    def __repr__(self):
        return self.question

@app.route('/quiz', methods=['GET', 'POST'])
def get_quiz():
    form = NumberForm()
    # A list to store questions
    questions_list = []
    # Store user's input for number of quizzes. Default = 0
    user_entered_number = form.number_of_quizzes.data
    api_url = f'https://jservice.io/api/random?count={user_entered_number}'
    response = requests.get(api_url)
    decoded_data = json.loads(response.text)
    print(response.status_code)
    # If request is successful
    if response.status_code == 200:
        for i in decoded_data:
            print(i['question'])
            quiz_question = i['question']
            q = Question.query.filter_by(question=quiz_question).first()
            # Evade adding duplicate questions
            while q is not None:
                response = requests.get(api_url)
                decoded_data = json.loads(response.text)
                quiz_question = i['question']
                q = Question.query.filter_by(question=quiz_question).first()
            # Add question to the database 
            question = Question(id=i['id'], 
                                question=i['question'],
                                answer=i['answer'],
                                created_at=i['created_at'])
            db.session.add(question)
            db.session.commit()
            questions_list.append(quiz_question)
    # Handle the errors
    elif response.status_code in [404, 500]:
        error_msg = f"Request failed with status code: {response.status_code}"
        print(error_msg)
    return render_template('index.html', form=form, questions_list=questions_list)

class NumberForm(FlaskForm):
    number_of_quizzes = StringField('How many quizzes?', default=0)
    submit = SubmitField('Send')

if __name__ == '__main__':
    app.run(debug=True)