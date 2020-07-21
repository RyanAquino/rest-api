# Simple REST API
> exposes 4 core values and 12 principles of Agile Software Development

## Technology 
* Python
* SQLAlchemy
* flask-restful
* MySQL


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
5. run server - `python app.py`


 