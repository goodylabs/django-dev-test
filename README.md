## Python/Django Developer Test
---
Simple Django project prepared for recruitment process.

Please clone this clean repository into your workspace, do some work and create a pull request.



### Requirements
---
- Python 3.7
- pipenv (https://github.com/pypa/pipenv)




### Project setup
---
##### Environment
Execute in project's root directory:

```
pipenv sync
```

Since now you can switch to virtual environment created by pipenv. To do so run `pipenv shell` command.

Otherwise you would have to add `pipenv run` prefix to every python-related command executed
within project's directory tree (see below).

##### Database setup
Execute in project's root directory:

```
pipenv run python manage.py migrate
pipenv run python manage.py createsuperuser
```

or

```
pipenv shell
./manage.py migrate
./manage.py createsuperuser
```

##### Start the app
Execute in project's root directory:
```
pipenv shell
./manage.py runserver
```



### Other tools
Please run a linter before pushing to the repo. To do so simply execute:
```
pipenv run flake8
```
...add fix any issues.
