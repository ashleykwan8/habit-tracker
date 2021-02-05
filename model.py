from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Todo(db.Model): 
    __tablename__= 'todos'
    id = db.Column(db.Integer, primary_key=True) 
    text = db.Column(db.String(200)) 
    complete = db.Column(db.Boolean) 
  
    def __repr__(self): 
        return f'<ToDo text={self.text} complete={self.complete}>'