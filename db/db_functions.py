from flask import jsonify, request
import sqlite3 as sql


# add a task
def db_add_task():
    try:
        with sql.connect("db/database.db") as database:
            admin = database.cursor()

            data = request.get_json()
            
            task_name = data['taskTitle']
            task_description = data['taskDescription']
            task_due_date = data['taskDueDate']

            admin.execute("INSERT INTO tasks (task_name, task_description, task_due_date) VALUES (?, ?, ?)", (task_name, task_description, task_due_date))
            database.commit()

        return jsonify({"message": "Task added"})

    except Exception as error:
        print(f"Error getting data from request: {error}")
        return jsonify({"error": "Error getting data from request"})
    

# update a task
def db_update_task(task_id):
    pass


# delete a task
def db_delete_task(task_id):
    try:
        with sql.connect("db/database.db") as database:
            admin = database.cursor()
            admin.execute("SELECT * FROM tasks WHERE task_id = ?", (task_id,))
            selected_data = admin.fetchone()
            if selected_data:
                print(f"Deleting task: {selected_data}")
                admin.execute( "DELETE FROM tasks WHERE task_id = ?", (task_id,))
                database.commit()
                return jsonify({"message": "Task Deleted"})

    except Exception as error:
        print(f"Error reading data from database; - db_delete_task: {error}")
        return jsonify({"error": "Error getting data from request"})
    
def db_complete_task(task_id):
    try:
        with sql.connect("db/database.db") as database:
            admin = database.cursor()
            admin.execute("SELECT * FROM tasks WHERE task_id = ?", (task_id,))
            selected_data = admin.fetchone()
            if selected_data:
                print(f"Completing task: {selected_data}")
                admin.execute("UPDATE tasks SET task_status = 'Done' WHERE task_id = ?", (task_id,))
                database.commit()
                return jsonify({"message": "Task Completed"})

    except Exception as error:
        print(f"Error updating task status in database; - db_complete_task: {error}")
        return jsonify({"error": "Error updating task status"})
# get a task


# get all tasks
def db_get_all_tasks():
    try:
        with sql.connect("db/database.db") as database:
            admin = database.cursor()
            admin.execute("SELECT * FROM tasks")
            data = admin.fetchall()
            refined_data = [{'id': row[0], 'name': row[1], 'description': row[2], 'status': row[3]} for row in data]
            print(refined_data)
            return refined_data
        
    except Exception as error:
        print(f"Error reading data from database; - db_get_all_tasks: {error}")

# get all tasks filtered by status or due
def db_get_filtered_tasks(filter):
    pass

if __name__ == "__main__":
    # db_add_task()
    db_delete_task(1)