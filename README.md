# PROJECT SERVER SIDE

## CREATE PROJECT AND CREATE ENVIROMENT
```cmd
> mkdir my_projects
  
> py -m venv myvenv
  
> myvenv\Scripts\Activate.bat
```
## INSTALL DJANGO AND PSYCOPG2
```cmd
> pip install django
```
```cmd
> pip install psycopg2 OR pip install psycopg2-binary
```
## GO IN PROJECT 
```cmd
> cd my_projects
```
```cmd
> django-admin startproject {project_name}

> python manage.py startapp {app_name}
```

## START SERVER
```cmd
> python manage.py runserver
```
<br><br><br>

## SETTING.py
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "{database_name}",
        "USER": "postgres",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```
```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "{app_name}",
    "{extensions...}",
]
```
