"""Create, Read, Update, Delete (CRUD) operations."""

from model import  db, Todo, connect_to_db

if __name__== '__main__':
    from server import app
    connect_to_db(app)

    
def add_todo(text,complete):
    """ToDo item"""

    todo = Todo(text=text, complete=False)
    db.session.add(todo)
    db.session.commit()

    return todo

def complete_item(id):
    """Set item to complete"""

    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = True

    db.session.add(todo)
    db.session.commit()

    return todo

def delete_list():
    """delete the todo list"""
    
    db.session.query(Todo).delete()
    db.session.commit()