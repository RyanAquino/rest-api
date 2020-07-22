# Simple REST API
> exposes 4 core values and 12 principles of Agile Software Development

## Technology 
* Python
* SQLAlchemy
* flask-restful
* MySQL
* pytest
* black formatting
* 


## Setup
> Note: Python / MySQL should be installed
1. create database with any name
2. fill out `rest_api/api/config.py` with Database details\
`USERNAME=<mysql username>` \
`PASSWORD=<mysql password>` \
`HOST=<mysql host>` \
`DB=<mysql database name>`

2. cd to project directory
3. run migrations - `python migrate db upgrade`
4. Populate database - `python seed.py`
5. create virtual env - `pipenv shell`
6. install required packages - `pipenv install`
7. run server - `python app.py`

## To run tests
> Note: be sure you are inside a virtual environment
1. `pipenv install --dev`
2. cd to `rest_api/tests`
3. run `pytest`


 