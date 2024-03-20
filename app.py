from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kaplandb.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))

    def __repr__(self):
        return f'<User: {self.name}>'

class Channels(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))

    def __repr__(self):
        return f'<Channel: {self.name}>'


@app.route('/get_all_users', methods=['POST'])
def get_all_users():
    print("Hello there we are getting all the users")

    users = Users.query.all()

    users_list = [{'id': user.id, 'name': user.name} for user in users]

    print(users_list)

    return users_list


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/About/<name>')
def about_name(name):
    return 'Hello %s!' % name

if __name__ == '__main__':
    app.run(debug = True)