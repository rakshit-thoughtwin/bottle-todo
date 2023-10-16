<!DOCTYPE html>
<html>
<head>
    <title>To-Do List</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }

        h1 {
            background-color: #333;
            color: #fff;
            padding: 10px;
            text-align: center;
        }

        form {
            background-color: #fff;
            padding: 10px;
            text-align: center;
            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
        }

        input[type="text"] {
            width: 70%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        button {
            padding: 10px 20px;
            background-color: #333;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background-color: #555;
        }

        ul {
            list-style-type: none;
            padding: 0;
        }

        li {
            background-color: #fff;
            padding: 10px;
            border: 1px solid #ccc;
            margin: 5px 0;
            display: flex;
            align-items: center;
            justify-content: space-between; /* Added for right alignment */
        }

        a {
            text-decoration: none;
            color: #333;
            font-size: 18px;
            margin-right: 10px;
        }

        a.completed {
            color: #5CB85C;
        }

        a.incomplete {
            color: #D9534F;
        }

        .delete-btn {
            color: #D9534F;
        }
    </style>
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
                <a href="/complete/{{ task[0] }}" class="{{ 'completed' if task[2] else 'incomplete' }}">{{ '✓' if task[2] else '□' }}</a>
                {{ task[1] }}
                <a href="/delete/{{ task[0] }}" class="delete-btn">Delete</a>
            </li>
        % end
    </ul>
</body>
</html>
