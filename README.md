# devopzilla-api
a simple RESTful CRUD API for a merchant application to manage 2 resources; items and orders

#### Install Dependencies
```sh
pip install pipenv
pipenv install
```

#### Configure Environment Variables
- Create .env file
```
POSTGRES_USER = <POSTGRES_USER>
POSTGRES_PASSWORD = <POSTGRES_PASSWORD>
POSTGRES_SERVER = <POSTGRES_SERVER>
POSTGRES_PORT = <POSTGRES_PORT>
POSTGRES_DB = <POSTGRES_DB>
```

## Run it

```sh
pipenv shell
uvicorn app.main:app
```

## Test it

```sh
pytest
```