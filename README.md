A small quiz

- Recommend to use virtual environment. 
To install it: 


python3 -m venv venv

- To activate the virtual environment source 


venv/bin/activate

- To install neccessary libraries:


pip install -r requirements.txt

- To run the app:


flask run

- Debug mode:

flask run --debug

NB: You don't need to set export FLASK_APP=microblog.py since I did it myself. You only need to install python-dotenv (requirements.txt)
