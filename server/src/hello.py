from flask import Flask
from flask import request
from flask_cors import CORS
import sqlite3
import os


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
         return createHTMLForQuestionList("Neetcode 150")
         # return '<li><input type="checkbox">3Sum</li>'
    else:
         return '<li><input type="checkbox">Sudoku</li>'

basedir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(basedir, '../../gato.db')

def createHTMLForQuestionList(question_list_name):
     # step 1: find the questions in the db for
     # this list name
     # connect to SQLite db
     con = sqlite3.connect(database_path)
     # the returned connection object represents
     # the connecton to the on-disk db.
     cur = con.cursor()
     # we need cursor to execute sql statements
     # and fetch results.
     cur.execute("SELECT list_id FROM lists WHERE list_name = ?", (question_list_name,))
     res = cur.fetchone()
     if not res:
          return 'Invalid list name', 400
     list_id = res[0]
     # fetch questions for given list id
     query = '''
     SELECT q.question_name, q.link, q.difficulty, q.topic
     FROM questions q
     JOIN questionInList ql ON q.question_id = ql.question_id
     WHERE ql.list_id = ?
     '''
     cur.execute(query, (list_id,))
     # list_id gets inserted instead of ?
     rows = cur.fetchall()
     print(f"Rows: {rows}")  # Debug print
     con.close()
     html_items = []
     for row in rows:
          qname, link, difficulty, topic = row
          html_item = f'''
          <li>
               <input type="checkbox">
               <a href="{link}" target="_blank">{qname}</a>
               <span class="topic">
               {topic}
               </span>
               <span class={difficulty}>
               {difficulty}
               </span>
          </li>
          '''
          html_items.append(html_item)
     return ''.join(html_items)

if __name__ == '__main__':
    app.run(debug=True)
    