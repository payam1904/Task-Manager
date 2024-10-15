from flask import jsonify, request
import sqlite3 as sql


# add a task
def db_add_task():
    # Create a new database connection for this thread


    try:
        with sql.connect("db/database.db") as database:
            # connection.row_factory = sql.Row
            admin = database.cursor()

            data = request.get_json()
            print(data)
            task_name = data['taskTitle']
            task_description = data['taskDescription']
            task_due_date = data['taskDueDate']

            admin.execute("INSERT INTO tasks (task_name, task_description, task_due_date) VALUES (?, ?, ?)", (task_name, task_description, task_due_date))
            database.commit()

        return jsonify({"message": "Task added"}), 200

    except Exception as error:
        print(f"Error getting data from request: {error}")
        return jsonify({"error": "Error getting data from request"}), 400
    
# delete a task

# update a task

# get a task

# get all tasks

# get all tasks by status

if __name__ == "__main__":
    db_add_task()