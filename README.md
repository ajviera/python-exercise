# Python Exercise

![logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

[![Build Status](https://travis-ci.org/ajviera/python-exercise.svg?branch=master)](https://travis-ci.org/ajviera/python-exercise)
[![Coverage Status](https://coveralls.io/repos/github/ajviera/python-exercise/badge.svg?branch=master)](https://coveralls.io/github/ajviera/python-exercise?branch=master)

## Requirements

- _Python_ > 3.6.3

## Set up project

`Docker`

The project is Docker-ready. To start developing we just need to have Docker installed.

``` sh
docker-compose build
docker-compose up
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

![uml](https://github.com/ajviera/python-exercise/blob/master/uml.png)

To model the domain of the problem, opt for Object Oriented Programming, using specifically Inheritance and Polymorphism in classes that share the same identity. This allowed me to maintain the modulation of the code without repeating it unnecessarily.

## Development Practices

First, I set up the [Git repository](https://github.com/ajviera/python-exercise), then I installed test and coverage tools, CI tools like [Travis](https://travis-ci.org/ajviera/python-exercise) and [Coveralls](https://coveralls.io/github/ajviera/python-exercise), and Dockerize the application. These are the things I usually do when I start developing a new project.
