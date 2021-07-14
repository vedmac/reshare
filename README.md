[![Actions Status](https://github.com/Bytlot/reshare/workflows/reshare/badge.svg)](https://github.com/Bytlot/reshare/actions)
[![Actions Status](https://github.com/Bytlot/reshare/workflows/CodeQL/badge.svg)](https://github.com/Bytlot/reshare/actions)


# Reshare

### Description
Reshare is a webapp that lets you create your own recipes and share them with other people. You can also subscribe to recipe authors and add recipes to your shopping list and download the list with all ingredients you need.

### Tech stack
- Python 3.9.5
- JavaScript
- Django and Django Rest Framework
- PostgreSQL
- Django ORM
- Gunicorn + Nginx
- Docker, docker-compose
- GitHub Actions
- JWT token authentication

---

### **Requirements**

Requirements before start:

[Docker](https://docs.docker.com/get-docker/)

[Docker-compose](https://docs.docker.com/compose/install/)

Set your environment with your settings in `.env` file:
```
# SAMPLE
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
DEBUG=False
LOCAL=True 
```

### Installing

Installing steps:

Build and run:
```
$ make start
```
Fill ingredients and tags:
``` 
$ make filldb
```
Create supruser:
```
$ make createsuperuser
```
Stop:
```
$ make stop
```

## Admin access

Admin panel available after project started at http://host/admin/