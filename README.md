Flask-Tornado-Chat
==================

[![Build Status](https://travis-ci.org/JosephViolago/Flask-Tornado-Chat.svg?branch=master&style=shield)](https://travis-ci.org/JosephViolago/Flask-Tornado-Chat?branch=master)
[![codecov](https://codecov.io/gh/JosephViolago/Flask-Tornado-Chat/branch/master/graph/badge.svg)](https://codecov.io/gh/JosephViolago/Flask-Tornado-Chat)

## Install

* **$** `sudo pip install virtualenv`
* Clone repo
* **$** `cd Flask-Tornado-Chat`
* **$** `virtualenv venv`
* **$** `. venv/bin/activate`
* **$** `pip install -r requirements.txt`

## Use

* Note: Your shell must be in the `venv` environment to run.
* **$** `python run.py`
* http://localhost:5000
* `Ctrl/Cmd + c` to shut down server
* **$** `deactivate` to leave virtualenv

## Test

* **$** `pytest`

## Trouble?

### "WARNING: The tornado.speedups extension module could not be compiled."

* **$** `sudo apt-get install build-essential python-dev`
* **$** `sudo yum install gcc python-devel`
* **$** `pip install -I --ignore-installed -r requirements.txt`
