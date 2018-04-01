# crudvehicles

## Requirements
* Python 3.6
* [pipenv](https://docs.pipenv.org/)

## Environment
* `export PIPENV_VENV_IN_PROJECT=1`
* `pipenv --python 3.6`
* `pipenv shell`
* `pipenv install`

* `python manage.py migrate`

## Execute project

* Pre populate database `python manage.py loaddata fixture/dump.json`

* Run server `python manage.py runserver`

* Access [http://localhost:8000/api/](http://localhost:8000/api/) for list all urls

## Execute test
* `pytest -v `
