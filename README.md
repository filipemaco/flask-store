# BUILD THE IMAGE
- docker build -t rest-apis-flask-python .

# RUN DOCKER -> PRODUCTION
- docker run -p 5005:5000 rest-apis-flask-python


# RUN DOCKER -> LOCALLY
- docker run -p 5005:5000 -w /app -v "$(pwd):/app" rest-apis-flask-python


# DATABASES - FLASK MIGRATE
- Create the database or enable migrations if the database already exists with the following command:
```
flask db init 
```

- Generate the migration:
```
flask db migrate 
```

- Apply the migration to the database:
```
flask db upgrade
```