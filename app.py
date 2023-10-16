from bottle import Bottle, template, request, redirect
import sqlite3

app = Bottle()

@app.route('/')
def index():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks ORDER BY completed, id")
    tasks = cursor.fetchall()
    conn.close()
    return template("views/index", tasks=tasks)


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


@app.route('/complete/<task_id>')
def complete_task(task_id):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed=1 WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    redirect('/')


@app.route('/delete/<task_id>')
def delete_task(task_id):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    redirect('/')

if __name__ == '__main__':
    app.run(host='localhost', port=8080)



