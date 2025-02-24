from flask import Flask, render_template, request
from helper import alert
import db

# Define the flask application
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """Provides the main page for task management"""
    cursor, conn = db.establish_conn()
    db.initialize_table(cursor)

    try:
        if request.method == "POST":
            if "task-text" in request.form:
                task_text = request.form.get("task-text", "").strip()
                if not task_text:
                    return alert("Please provide the task text", 400)
                try:
                    db.add_task(cursor, task_text)
                    conn.commit()
                except Exception as e:
                    return alert(f"Error adding task: {str(e)}", 500)
            elif "delete" in request.form:
                task_id = int(request.form["delete"])
                db.remove_task(cursor, task_id)
                conn.commit()  # Ensure to commit after delete
        # GET
        tasks = db.query_tasks(cursor)
    finally:
        cursor.close()  # Close the cursor
        conn.close()  # Close the connection

    return render_template("index.html", tasks=tasks)


# TODO: Login page
# TODO: Register page
# TODO: Export data
