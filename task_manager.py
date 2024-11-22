# task_manager.py

import sqlite3 # in-built database for python

DB_NAME = "tasks.db"

def setup_database():
    """Initialize the database and create tables if they don't exist."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        # Create the tasks table if it doesn't already exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL
            )
        """)
        conn.commit()


def add_task_to_db(task):
    """Add a task to the database."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (description) VALUES (?)", (task,))
        conn.commit()
    return f"Task '{task}' added successfully."

def delete_task_from_db(task):
    """Delete a task from the database."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE description = ?", (task,))
        if cursor.rowcount > 0:
            conn.commit()
            return f"Task '{task}' deleted successfully."
        else:
            return f"Task '{task}' not found."

def list_tasks_from_db():
    """Retrieve all tasks from the database."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT description FROM tasks")
        tasks = cursor.fetchall()
    if not tasks:
        return "No tasks available."
    return "\n".join([f"{i+1}. {task[0]}" for i, task in enumerate(tasks)])
