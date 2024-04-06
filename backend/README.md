# Content Management Syste - FastAPI - Backend

## How to start the application

1. Now Activate a python virtual environment
```
$ source active/bin/activate
```

2. Move to the backend directory
```
$ cd backend
```

3. Now install all the requirements
```
$ pip install -r ./requirements.txt
```

4. Now start the application
```
$ uvicorn app.main:app --reload
```

Now finally navigate the ```127.0.0.1:8000/```.

## Alembic Integration

Integrate Alembic with project using the following command. <br />
```
$ init alembic
```

1. Alembic makemigration command
```
$ alembic revision --autogenerate -m "commit message"
```

2. Alembic migrate command
```
$ alembic upgrade head
```

**Use alembic migration after every database model changes.**

## Code Implementation
1. Create boilerplate code with **main.py**.
2. Connect with the database.
3. Add Alembic for database migration.
4. Create [Models and Schemas](#for-aPIs-implementation)
5. Create CRUD Utils (repository) and Implement the route.

## For APIs Implementation

URL - https://fastapi.tiangolo.com/tutorial/sql-databases/

These steps are according to this doc.

1. Create SQLAlchemy model [models]
2. Create Pydantic model [schemas]
3. CRUD Utils [repository]
