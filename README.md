# Simple REST API
> exposes 4 core values and 12 principles of Agile Software Development

## Technology 
* Python
* SQLAlchemy
* flask-restful
* MySQL
* pytest
* black formatting
* Mypy


## Setup
> Note: Python / MySQL should be installed
1. create database with any name
2. fill out `rest-api/api/config.py` with Database details\
`USERNAME=<mysql username>` \
`PASSWORD=<mysql password>` \
`HOST=<mysql host>` \
`DB=<mysql database name>`

3. cd to project directory
4. create virtual env - `pipenv shell`
5. install required packages - `pipenv install`
6. run migrations - `python migrate db upgrade`
7. Populate database - `python seed.py`
8. run server - `python app.py`

## To run tests
> Note: be sure you are inside a virtual environment
1. `pipenv install --dev`
2. run `pytest` in project root directory


 