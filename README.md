Task was provided with broken json file - the one with "_updated" suffix is correct

Project created and optimized for Postgresql@14.

### Getting started

It is necessary to run all commands below in root directory (where `requirements.txt` is located).

At first, it is recommended to create virtual environment to run this code. More info here: [creating venv python](https://docs.python.org/3/library/venv.html).

Installing requirements:

```
pip install -r requirements.txt
```

Environment variables to configure database access:
```
POSTGRES_USER
POSTGRES_PASSWORD
DATABASE_HOST
POSTGRES_DB
```
It is possible to configure env variable for list of instance keys, that we want to parse and push to database in following format:
```
KEYS_TO_DATABASE="Port-channel,TenGigabitEthernet,GigabitEthernet"
```

Environment variable for path to config.json file:

```
PATH_TO_FILE
```

Database is created using docker container: 

1. [Setting up docker](https://docs.docker.com/desktop/)

2. Building container

```
docker-compose build
``` 
3. Starting container

```
docker-compose up
```

After setting all of these prerequisites, program is ready to start by

```
python main.py
```


### Migrations
Creating new migration:
```
alembic revision --autogenerate
```

Commit created migrations into database:
```
alembic upgrade head
```