# PROJECT SERVER SIDE

## SETUP FOR DIRECTORY
### CREATE PROJECT AND CREATE ENVIROMENT
```cmd
> mkdir my_projects
  
> py -m venv myvenv
  
> myvenv\Scripts\Activate.bat
```
### INSTALL DJANGO AND PSYCOPG2
```cmd
> pip install django
```
```cmd
> pip install psycopg2 OR pip install psycopg2-binary
```
### GO IN PROJECT 
```cmd
> cd my_projects
```
```cmd
> django-admin startproject {project_name}

> python manage.py startapp {app_name}
```

### START SERVER
```cmd
> python manage.py runserver
```
<br>

### SETTING.py
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
    ## ถ้ามีการใช้ jupyter
    "django_extensions",
]
```
<br><br><br><br>
## SETUP FOR JUPYTER NOTEBOOK
###
```cmd
> pip install django-extensions ipython jupyter notebook

> pip install ipython==8.25.0 jupyter_server==2.14.1 jupyterlab==4.2.2 jupyterlab_server==2.27.2

> pip install notebook==6.5.7
```
```cmd
> mkdir notebooks
```
```cmd
> python manage.py shell_plus --notebook
```

### IMPORT
```python
import os
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
```
```python
from {app_name}.models import * -{class_name}
from django.db.models import F, Q, Count, Value as V, AVG, MAX, MIN, OuterRef, Subquery, Sum
from django.db.models.functions import Now, Concat
import datetime as datetime
```




