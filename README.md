# Python Exercise

<p align="center">
  <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"/>
</p>

[![Build Status](https://travis-ci.org/ajviera/python-exercise.svg?branch=master)](https://travis-ci.org/ajviera/python-exercise)
[![Coverage Status](https://coveralls.io/repos/github/ajviera/python-exercise/badge.svg?branch=master)](https://coveralls.io/github/ajviera/python-exercise?branch=master)

## Requirements

- _Python_ > 3.6.3

## Set up project

`Docker`

The project is Docker-ready. To start developing we just need to have Docker installed.

``` sh
docker-compose build
docker-compose up -d && docker attach intive-fdv_app
```

And that's it :-)

`Linux`

```sh
virtualenv intive-fdv --python=python3.6
git clone git@github.com:ajviera/python-exercise.git
source bin/activate
cd python-exercise
pip install -r requirements.pip
```

`MacOS`

```sh
pyenv virtualenv 3.6.3 intive-fdv
git clone git@github.com:ajviera/python-exercise.git
pyenv activate intive-fdv
cd python-exercise
pip install -r requirements.pip
```

## Update requirements

```sh
pip freeze > requirements.pip
```

## Run Test with Coverage

with Docker

```sh
docker-compose run --rm intive-fdv_app coverage run --source=src/models -m unittest tests/models/*.py && docker-compose run --rm intive-fdv_app coverage report
```

without Docker

```sh
coverage run --source=src/models -m unittest tests/models/*.py && coverage report
```

## Run Test without Coverage

with Docker

```sh
docker-compose run --rm intive-fdv_app python -m unittest tests/models/*.py
```

without Docker

```sh
python -m unittest tests/models/*.py
```

## Design

`Diagram`

<p align="center">
  <img src="https://github.com/ajviera/python-exercise/blob/master/uml.png"/>
</p>

To model the domain of the problem, opt for Object Oriented Programming, using specifically Inheritance and Polymorphism in classes that share the same identity. This allowed me to maintain the modulation of the code without repeating it unnecessarily.

## Development Practices

First, I set up the [Git repository](https://github.com/ajviera/python-exercise), then I installed test and coverage tools, CI tools like [Travis](https://travis-ci.org/ajviera/python-exercise) and [Coveralls](https://coveralls.io/github/ajviera/python-exercise), and Dockerize the application. These are the things I usually do when I start developing a new project.

## API DOC

---

### GET methods

> _GET users_
- `http://localhost:8080/api/v1/users`

> _GET user_
- `http://localhost:8080/api/v1/users/:id`

> _GET user rents_
- `http://localhost:8080/api/v1/users/:id/rents`

> _GET user rent_
- `http://localhost:8080/api/v1/users/:id/rents/:id`

---

### POST methods

> _POST create user rent_
- `http://localhost:8080/api/v1/users/:id/rents`

Expected Params:

```json
{
  "time": string, OPTIONS("per_hour", "per_day", "per_week")
  "extra_users": [ { "id": integer } ],
  "bike_id": 1,
  "type": string OPTIONS("normal", "family")
}
```

> _POST close user rent_
- `http://localhost:8080/api/v1/users/:id/rents/:id`