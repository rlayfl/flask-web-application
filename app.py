from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from datetime import datetime

import json
import urllib.parse

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
    description = db.Column(db.String())
    startDate = db.Column(db.DateTime())
    endDate = db.Column(db.DateTime())

    def __repr__(self):
        return f'<Module: {self.name}>'


# I have left this here as an example of how to set up a function to call with Ajax

# @app.route('/get_all_modules', methods=['POST'])
# def get_all_modules():
#     print("Hello there we are getting all the users")

#     modules = Modules.query.all()
#     modules_list = [{'id': module.id, 'name': module.name} for module in modules]

#     print(modules_list)

#     return modules_list
    

@app.route("/addNewModule", methods=['POST'])
def add_new_module():
    print("Adding new module to the database")

    print(str(request.data))

    # Decode URL-encoded string
    decoded_string = urllib.parse.unquote(request.data.decode())

    # Extract JSON part
    json_string = decoded_string.split('=', 1)[1]

    # Parse JSON string to JSON object
    json_object = json.loads(json_string)

    # Print JSON object
    print(json_object["code"])
    print(json_object["name"])
    print(json_object["description"])
    print(json_object["startDate"])
    print(json_object["endDate"])

    newModule = Modules(
        name=json_object["name"],
        code=json_object["code"],
        description=json_object["description"],
        startDate=datetime.strptime(json_object["startDate"], '%Y-%m-%d'),
        endDate=datetime.strptime(json_object["endDate"], '%Y-%m-%d')
    )

    db.session.add(newModule)
    db.session.commit()

    return "Hello"






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