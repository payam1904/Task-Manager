from flask import Flask, render_template,redirect, url_for, request
from db import db_functions

app = Flask(__name__, template_folder='templates', static_folder='static')


# @app.route('/home')
# def home():
#     return render_template('home.html')


@app.route('/')
def task_manager_project():
    data = db_functions.db_get_all_tasks()
    return render_template('task_manager.html', data=data)

@app.route('/task-manager/create-task', methods=['POST'])
def create_task():
    db_functions.db_add_task()
    return redirect(url_for('task_manager_project'))


# @app.route('/task-manager/delete-task')
# def delete_task():
#     db_functions.db_delete_task(1)
#     return redirect('task_manager.html')

@app.route('/task-manager/delete-task', methods=['GET'])
def delete_task():
    task_id = request.args.get('id')
    db_functions.db_delete_task(task_id)
    return redirect(url_for('task_manager_project'))

@app.route('/task-manager/complete-task', methods=['GET'])
def complete_task():
    task_id = request.args.get('id')
    db_functions.db_complete_task(task_id)
    return redirect(url_for('task_manager_project'))




if __name__ == '__main__':
    app.run(debug=True)