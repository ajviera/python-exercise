# Python Exercise

[![Coverage Status](https://coveralls.io/repos/github/ajviera/python-exercise/badge.svg)](https://coveralls.io/github/ajviera/python-exercise)

## Requirements

- _Python_ > 3.6.3

## Set up project

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

```sh
coverage run -m unittest tests/user_test.py && coverage report
```

## Run Test without Coverage

```sh
python -m unittest tests/*.py
```