import db_connection

connection = db_connection.database
db_admin = db_connection.admin


def create_tasks_table():
    try:
        connection.execute("""
            CREATE TABLE tasks (
                task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_name TEXT NOT NULL,
                task_description TEXT NOT NULL,
                task_status BOOLEAN DEFAULT 'Pending',
                task_created_date DATE DEFAULT CURRENT_TIMESTAMP,
                task_due_date DATE
                )""")
        connection.close()
    
    except db_connection.sql.OperationalError as error:
        print(f"Error creating tasks table: {error}")
        connection.close()

if __name__ == "__main__":
    create_tasks_table()