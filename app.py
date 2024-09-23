from flask import Flask, render_template,jsonify, request
from db import db_functions

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/task-manager')
def task_manager_project():
    return render_template('task_manager.html')

@app.route('/task-manager/create-task', methods=['POST'])
def create_task():

    db_functions.db_add_task()
    return render_template('task_manager.html')







if __name__ == '__main__':
    app.run(debug=True)