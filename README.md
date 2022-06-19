# Django Rest Framework + PostgreSQL
In this projects I built some features related to restaurants recipes.


## Dependencies
* Python ^3.9
* Poetry https://python-poetry.org/docs/configuration/
* Docker
* Docker compose

Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. It's like a pip + venv, all together.


## How to run using manage.py
Activate virtual environment
```bash
poetry shell
```

Install dependencies
```bash
poetry install
```

Up database
```bash
docker-compose up db -d
```

Run application
```bash
python manage.py
```

## How to run in docker
Run application
```bash
docker-compose up -d
```
