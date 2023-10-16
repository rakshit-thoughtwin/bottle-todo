<!DOCTYPE html>
<html>
<head>
    <title>To-Do List</title>
</head>
<body>
    <h1>To-Do List</h1>
    <form method="post" action="/add">
        <input type="text" name="task" placeholder="Add a new task" required>
        <button type="submit">Add</button>
    </form>
    <ul>
        % for task in tasks:
            <li>
                <a href="/complete/{{ task[0] }}">{{ '✓' if task[2] else '□' }}</a>
                {{ task[1] }}
            </li>
        % end
    </ul>
</body>
</html>
