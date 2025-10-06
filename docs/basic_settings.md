## basic_settings.md(using uv)

### uv 
```
$> pip install uv

$> mkdir <project name>
$> cd <project name>

$> uv init      # uv를 사용한 가상환경 자동 생성
$> .venv\Scripts\activate   # .venv 로 가상환경 활성화
(venv name) $> uv add Django

# running local dev server 
$> uv run manage.py runserver
```

## basic_settings.md(using pip)
- A document for basic envirionment instruction

### venv
- When using python package 
```
- windows 
$> python -m venv <venv name>
$> <venv name>\Scripts\activate

- linux/mac 
$> python3 -m venv <venv name>
$> source <venv name>/bin/activate

```
- When using Conda
```
- conda
$> conda create -n <venv name> python=<python version>\
$> conda env list 
$> conda activate <venv name>
```

## Django Setting
- Django install
```
$> python -m django --version
```

- Create project
```
$> django-admin startproject <project name> <project directory>
```

- Create apps
```
$> python manage.py startapp <app_name>
```

- settings.py / INSTALLED_APPS 
```
INSTALLED_APPS = [
    ...
    '<app_name>.apps.UsersConfig',
]
```


### Django REST Framework
- pip install
```
$> pip install djangorestframework 
```

- settings.py / INSTALLED_APPS 
```
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```