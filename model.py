from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Todo(db.Model): 
    __tablename__= 'todos'
    id = db.Column(db.Integer, primary_key=True) 
    text = db.Column(db.String(200)) 
    complete = db.Column(db.Boolean) 
  
    def __repr__(self): 
        return f'<ToDo text={self.text} complete={self.complete}>'

def connect_to_db(flask_app, db_uri='postgresql:///planner', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')
    
if __name__ == '__main__':
    from server import app

    connect_to_db(app)