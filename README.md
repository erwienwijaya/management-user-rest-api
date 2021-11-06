<p align="center"><a href="https://www.djangoproject.com/" target="_blank"><img src="https://static.djangoproject.com/img/logos/django-logo-positive.svg" width="400"></a></p>


# Management User Rest-API

Requirement development:

- Python >= 3.9.5
- Django 3.2.9
- SQLite3
- Virtualenv 20.4.7

## Installation

- Clone this repository `git clone git@github.com:erwienwijaya/management-user-rest-api.git`
- Install virtual environment: `pip3 install virtualenv`
- Create virtual environment: `virtualenv -p python3 venv` or `virtualenv -m python3 venv` 
- Activate virtualenv `source venv/bin/activate`
- Install requirements dependencies: `pip install -r requirements.txt`
- Run django server: `python3 manage.py runserver`
- Access the project at: `http://localhost:8000`

## Documentation
- Access the API documentation at: `http://localhost:8000/api/documentation`
- How to Authorize : `Bearer <token>`