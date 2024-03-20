from flask import Flask, render_template
import sqlite3

# Service Functions

app = Flask(__name__)

@app.route('/create_database_if_not_exists', methods=['POST'])
def create_database_if_not_exists():
    print("Hello this is a test")
    conn = sqlite3.connect('kaplan_modules.db')
    #return conn
    conn.close()

    response = {
        "test": "Bananas"
    }

    return response

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/About/<name>')
def about_name(name):
    return 'Hello %s!' % name

if __name__ == '__main__':
    app.run(debug = True)