from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# allow cors for all domains on all routers
# can allow specific cors later:
# https://flask-cors.readthedocs.io/en/3.0.10/


@app.route('/')
def hello():
	return 'meow'

@app.route('/question-lists', methods=['GET'])
def get_question_list():
	# based on list name, generate an HTML file
	# with list items with each question's data
    list_name = request.args.get('question-list-select')
    if list_name == 'neetcode-150':
         return '<li>3Sum</li>'
    else:
         return '<li>Sudoku</li>'

if __name__ == '__main__':
    app.run(debug=True)
