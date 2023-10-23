A small web app that displays a list of quizzes according to user's input and stores questions to the database

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


NB: You don't need to set export FLASK_APP= since I did it myself. You only need to install python-dotenv (requirements.txt)
