# Clone project
```
git clone https://github.com/heywhereismymind/todolist.git
```

# Create virtual env and activate
```
python -m venv .venv
./.venv/Scripts/Activate.ps1 (for Windows)
```

# Install packages
```
cd todolist
pip install -r requirements.txt
```

# Create migrations
```
python manage.py makemigrations
python manage.py migrate
```

# Run app
```
python manage.py runserver
```

# Endpoint
```
http://127.0.0.1:8000/api/v1/tasks/
```
