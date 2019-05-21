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
    ├── myproject
    │   ├── auth
    │   │   ├── controllers.py
    │   │   ├── forms.py
    │   │   ├── __init__.py
    │   │   ├── models.py
    │   │   └── routes.py
    │   ├── helpers
    │   │   ├── controllers.py
    │   │   ├── __init__.py
    │   │   └── models.py
    │   ├── __init__.py
    │   └── ui
    │       └── templates
    │           ├── 404.html
    │           ├── 500.html
    │           └── base.html
    ├── tests
    │   ├── auth
    │   │   ├── __init__.py
    │   │   └── test_controllers.py
    │   └── __init__.py
    ├── config.py
    ├── instance
    │   └── config.py
    ├── wsgi.py
    ├── README.md
    └── requirements.txt



## Bootstrapping

- Once app is created, do NOT forget to change SECRET_KEY from `instance/config.py`


## References

- [Flask](http://flask.pocoo.org)
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)
