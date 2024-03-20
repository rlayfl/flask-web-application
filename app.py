from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kaplandb.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

migrate = Migrate(app, db)

class ModuleEnrolments(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userAccountID = db.Column(db.Integer)
    ModuleID = db.Column(db.Integer)

    def __repr__(self):
        return f'<Module Enrolment: {self.id}>'

class UserAccounts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())

    def __repr__(self):
        return f'<User: {self.name}>'

class Modules(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    code = db.Column(db.String())
    startDate = db.Column(db.DateTime())
    endDate = db.Column(db.DateTime())

    def __repr__(self):
        return f'<Module: {self.name}>'




@app.route('/get_all_modules', methods=['POST'])
def get_all_modules():
    print("Hello there we are getting all the users")

    modules = Modules.query.all()
    modules_list = [{'id': module.id, 'name': module.name} for module in modules]

    print(modules_list)

    return modules_list


@app.route('/')
def index():

    modules = Modules.query.all()
    modules_list = [{'id': module.id, 'name': module.name} for module in modules]

    print(modules_list)

    return render_template("index.html", modules = Modules.query.all())

@app.route('/About/<name>')
def about_name(name):
    return 'Hello %s!' % name

if __name__ == '__main__':
    app.run(debug = True)