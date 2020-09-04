# Simple REST API
> exposes 4 core values and 12 principles of Agile Software Development

## Technology 
* Python
* MySQL
* SQLAlchemy
* Flask
* Pytest
* Swagger UI
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
6. run migrations - `python migrate.py db upgrade`
7. Populate database - `python seed.py`
8. run server - `python app.py`

## Docker setup (alternative)
1. run `docker-compose up -d` in project root directory
2. migrate and populate db - `docker exec -it flask /bin/sh -c "python migrate.py db upgrade && python seed.py"`

## To run tests
> Note: be sure you are inside a virtual environment
1. `pipenv install --dev`
2. run `pytest` in project root directory

## Access Swagger UI documentation
> Note: Be sure server is running
* access through browser with http://localhost:5000/swagger


