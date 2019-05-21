# Cookiecutter skeleton for Flask application


## Requirements

- python (Tested on 3.6.6 . For 2.x.x, requirements and some 'import' could be changed)
- cookiecutter (`pip install cookiecutter`)


## Usage


### Method 1 using remote url

    > cookiecutter https://github.com/rohitchormale/cookiecutter-flask 
    project_slug [myproject]: /opt/fooproject (Enter new project name with proper path. If empty 'myproject' will be used with current directory)
    author[]: John Smith( Enter author name. If empty, empty string will be used)
    > cd <project-path>
    > flask run


### Method 2 from source

    > git clone https://github.com/rohitchormale/cookiecutter-flask 
    > cookiecutter <absolute-path-to-cloned-repo>
    project_slug [myproject]: /opt/fooproject (Enter new project name with proper path. If empty 'myproject' will be used with current directory)
    author[]: John Smith( Enter author name. If empty, empty string will be used)
    > cd <project-path>
    > flask run


## Skeleton Structure
   

     myproject
     ├── myapp
     │   ├── __init__.py
     │   ├── extensions.py
     │   │
     │   ├── helpers
     │   │   ├── __init__.py
     │   │   ├── controllers.py
     │   │   ├── models.py
     │   │   └── commands.py
     │   │
     │   ├── auth
     │   │   ├── __init__.py
     │   │   ├── routes.py
     │   │   ├── controllers.py
     │   │   ├── models.py
     │   │   ├── forms.py
     │   │   └── commands.py
     │   │
     │   └── ui
     │       ├── static
     │       │   ├── css
     │       │   │   └── styles.css
     │       │   └── js
     │       │       └── custom.js
     │       │
     │       └── templates
     │           ├── 404.html
     │           ├── 500.html
     │           └── base.html
     │
     ├── tests
     │   ├── __init__.py
     │   ├── conftest.py
     │   │   
     │   └── auth
     │       ├── __init__.py
     │       └── test_controllers.py
     │
     ├── config.py
     ├── instance
     │   └── config.py
     ├── wsgi.py
     │
     ├── requirements.txt
     └── README.md 



## Bootstrapping

- Once app is created, do NOT forget to change SECRET_KEY from `instance/config.py`


## References

- [Flask](http://flask.pocoo.org)
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)
