# Cookiecutter skeleton for Flask application


## Requirements

- python (Tested on 3.6.6 . For 2.x.x, requirements and some 'import' could be changed)
- cookiecutter (`pip install cookiecutter`)


## Usage


### Method 1 from source

    > git clone git@github.com:rohitchormale/flask-skeleton-cookiecutter.git
    > cookiecutter <absolute-path-to-cloned-repo>
    project_slug [myproject]: /opt/fooproject (Enter new project name with proper path. If empty 'myproject' will be used with current directory)
    author[]: John Smith( Enter author name. If empty, empty string will be used)
    > cd <project-path>
    > python development.py

### Method 2 using remote url

    > cd <directory-where-you-want-project>
    > cookiecutter git@github.com:rohitchormale/flask-skeleton-cookiecutter.git
    project_slug [myproject]: /opt/fooproject (Enter new project name with proper path. If empty 'myproject' will be used with current directory)
    author[]: John Smith( Enter author name. If empty, empty string will be used)
    > cd <project-path>
    > python development.py


## Bootstrapping

- Once app is created, do NOT forget to change SECRET_KEY from `instance/config.py`


## References

- [Flask](http://flask.pocoo.org)
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)
