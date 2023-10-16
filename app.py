from bottle import Bottle, template, request, redirect
import sqlite3

app = Bottle()

# Route to display tasks
@app.route('/')
def index():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks ORDER BY completed, id")
    tasks = cursor.fetchall()
    conn.close()
    return template("views/index", tasks=tasks)

# Route to add a new task
@app.route('/add', method='POST')
def add_task():
    new_task = request.forms.get('task')
    if new_task:
        conn = sqlite3.connect("tasks.db")

        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (task, completed) VALUES (?, 0)", (new_task,))
        conn.commit()
        conn.close()
    redirect('/')

# Route to mark a task as completed
@app.route('/complete/<task_id>')
def complete_task(task_id):
    conn = sqlite3.connect("tasks.db")

    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed=1 WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    redirect('/')

if __name__ == '__main__':
    app.run(host='localhost', port=8080)


import sqlite3

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE tasks (id INTEGER PRIMARY KEY, task TEXT, completed INTEGER)")
conn.commit()
conn.close()