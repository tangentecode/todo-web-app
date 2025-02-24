from flask import Flask, render_template, request
from helper import alert
import db

# Define the flask application
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """Provides the main page for task managment"""
    cursor, conn = db.establish_conn()
    db.initialize_table(cursor)

    if request.method == "POST":
        task_text = request.form.get("task-text", "").strip()
        if not task_text:
            return alert("Please provide the task text", 400)
        try:
            db.add_task(cursor, task_text)
            conn.commit()
        except Exception as e:
            return alert(f"Error adding task: {str(e)}", 500)
    # GET
    tasks = db.query_tasks(cursor)
    return render_template("index.html", tasks=tasks)


# TODO: Login page
# TODO: Register page
# TODO: Export data
