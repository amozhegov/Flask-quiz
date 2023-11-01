**Quiz web app with Python Flask, API integration, and SQLite database.**


This web app that displays a list of quizzes from API according to user's input and stores data to the database

- Recommend to use virtual environment. 
To install it: 


python3 -m venv venv

- To activate the virtual environment source 


venv/bin/activate

- To install neccessary libraries:


pip install -r requirements.txt


- To install sqlite3:

sudo apt install sqlite3

- To see all database entries:

select * from question;

- To run the app:


flask run

- Debug mode:

flask run --debug

- To install Docker-compose

sudo apt install docker-compose




How to build docker image:

Create a docker file and add this code

- Use a base Python image
  
FROM python:3.8-slim

- Install system dependencies
  
RUN apt-get update -y && apt-get install -y libpq-dev

- Install Python dependencies
  
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

- Copy the application into the container

COPY . /app/

- Define an environment variable for Flask

  
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

- Create the database and apply migrations (if necessary)

  
RUN flask db init
RUN flask db migrate
RUN flask db upgrade

- Run the application

  
CMD ["flask", "run"]


NB: You don't need to set export FLASK_APP= since I did it myself. You only need to install python-dotenv (requirements.txt)
