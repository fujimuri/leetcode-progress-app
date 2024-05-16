from flask import Flask
from flask import request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
# allow cors for all domains on all routers
# can allow specific cors later:
# https://flask-cors.readthedocs.io/en/3.0.10/

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)

@app.route('/')
def hello():
	return 'meow'

@app.route('/question-lists', methods=['GET'])
def get_question_list():
	# based on list name, generate an HTML file
	# with list items with each question's data
    list_name = request.args.get('question-list-select')
    if list_name == 'neetcode-150':
         return '<li><input type="checkbox">3Sum</li>'
    else:
         return '<li><input type="checkbox">Sudoku</li>'
    
def createHTMLForQuestionList(question_list):
     # this function receives a list of questions
     # and creates the appropriate HTML where
     # each question becomes a <li> checkbox item
     # which has the question name, link, and
     # difficulty level
     # the question_list will be received from
     # the database. i think SQLite will do for now.
     return

if __name__ == '__main__':
    app.run(debug=True)