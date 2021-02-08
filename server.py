
from flask import Flask
from flask import (Flask, render_template, request, flash, session,
                   redirect)
from jinja2 import StrictUndefined
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
import random
from model import Todo

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def create_todo_list():
    """Show Todo List"""

    incomplete = Todo.query.filter_by(complete=False).all()
    complete = Todo.query.filter_by(complete=True).all()
    
    return render_template('index.html', 
                        incomplete=incomplete, 
                        complete=complete)


@app.route('/add', methods=["POST"])
def add_item():
    """Add item to ToDo List"""

    item = request.form.get('todoitem')
    crud.add_todo(item, False)

    return redirect('/')


@app.route('/complete/<id>')
def complete_item(id):

    crud.complete_item(id)

    return redirect('/')


@app.route('/delete')
def delete_list():
    """Delete complete items"""

    crud.delete_list()

    return redirect('/')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)