## basic_settings.md
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


### Django
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

