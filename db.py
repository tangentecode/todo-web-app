import sqlite3
from typing import Dict


def establish_conn() -> (sqlite3.Cursor, sqlite3.Connection):
    # Establishing connection
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    return (cursor, conn)


def initialize_table(cursor: sqlite3.Cursor) -> None:
    """
    Table Layout:
    id  task
    """
    # Create table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_text TEXT NOT NULL
        )
        """
    )


def add_task(cursor: sqlite3.Cursor, task_text: str) -> None:
    """Adds task entry to database"""
    cursor.execute("INSERT INTO tasks (task_text) VALUES (?)", (task_text,))


def remove_task(cursor: sqlite3.Cursor, task_id: int) -> None:
    """Removes task entry by id"""
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))


def query_tasks(cursor: sqlite3.Cursor) -> Dict[int, str]:
    """Returnes all tasks in a proper format"""
    # Querying data
    cursor.execute("SELECT * FROM tasks")
    results = cursor.fetchall()  # Fetch all rows

    # Fomat data to dict format
    results_dict = dict(results)
    print(results_dict)
    return results_dict


#  TODO: Edit tasks


def close_conn(conn: sqlite3.Connection) -> None:
    """Save and close the connection"""
    conn.commit()
    conn.close()


# For debugging purposes
def main() -> None:
    cursor, conn = establish_conn()

    initialize_table(cursor)
    add_task(cursor, "this is test number one")
    add_task(cursor, "this is test number two")
    add_task(cursor, "this is test number three")
    remove_task(cursor, 1)
    query_tasks(cursor)
    close_conn(conn)


if __name__ == "__main__":
    main()
