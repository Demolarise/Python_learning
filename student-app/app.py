import os
import sqlite3

from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)

# When running in Docker this will become:
# /data/students.db
DATABASE = os.environ.get("DATABASE", "./data/students.db")


def get_db_connection():
    connection = sqlite3.connect(
        DATABASE,
        timeout=10
    )

    connection.row_factory = sqlite3.Row

    return connection


def init_db():

    database_directory = os.path.dirname(DATABASE)

    if database_directory:
        os.makedirs(database_directory, exist_ok=True)

    connection = get_db_connection()

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER,
            course TEXT NOT NULL
        )
        """
    )

    connection.commit()
    connection.close()


# Initialise the database when the application starts
init_db()


@app.route("/")
def index():

    connection = get_db_connection()

    students = connection.execute(
        """
        SELECT id, name, email, age, course
        FROM students
        ORDER BY id DESC
        """
    ).fetchall()

    connection.close()

    return render_template(
        "index.html",
        students=students
    )


@app.route("/students", methods=["POST"])
def add_student():

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    age = request.form.get("age", "").strip()
    course = request.form.get("course", "").strip()

    if not name or not email or not course:
        return "Name, email and course are required.", 400

    if age:
        try:
            age = int(age)
        except ValueError:
            return "Age must be a number.", 400
    else:
        age = None

    connection = get_db_connection()

    connection.execute(
        """
        INSERT INTO students (
            name,
            email,
            age,
            course
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            name,
            email,
            age,
            course
        )
    )

    connection.commit()
    connection.close()

    return redirect(url_for("index"))


@app.route(
    "/students/<int:student_id>/delete",
    methods=["POST"]
)
def delete_student(student_id):

    connection = get_db_connection()

    connection.execute(
        """
        DELETE FROM students
        WHERE id = ?
        """,
        (student_id,)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5050,
        debug=False
    )