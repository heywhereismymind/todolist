# Clone project
```
git clone https://github.com/heywhereismymind/todolist.git
```

# Create virtual env and activate
```
python -m venv .venv
./.venv/Scripts/Activate.ps1 (for Windows)
```

# Create database PostgreSQL

# Create .env file and write data like .env-example

# Create migrations
```
cd to_do_list
python manage.py makemigrations
python manage.py migrate
```

# Run app
```
python manage.py runserver
```

# Examples
> Endpoint : http://127.0.0.1:8000/todo/api/v1.0/tasks  
>Method GET: get list of tasks  
>Method POST: add task to list
>- headers : Content-Type - application/json
>- body :  
{     
    "task_name": str,  
    "task_description": str  
} 
>  
>Endpoint : http://127.0.0.1:8000/todo/api/v1.0/tasks/{task_id}  
>Method GET: get task by id  
>Method DELETE: delete task by id  
>Method PUT: update task by id
>- headers : Content-Type - application/json
>- body :  
{     
    "task_name": str,  
    "task_description": str  
} 
