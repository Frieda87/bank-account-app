# Bank Account App: Backend

Building a web app using Python, Flask. It follows typical RESTful API design pattern.

## SETUP

I assume you already installed Python 3.4 or higher and pip.

### Virtual Environment

Install virtualenv via pip:

```
$ pip3 install virtualenv
```

Create a virtual environment for a project:

```
$ cd bank-account-app
$ python3 -m venv venv
```

To begin using the virtual environment, it needs to be activated:

```
$ source venv/bin/activate
```

Install the same packages using the same versions:

```
(venv) $ pip3 install -r requirements.txt
```

### Database

Before you run the server, you will have to create a database and a User model
First, go to the Python shell (while you are in your virtualenv) and import the database from crazyshit:

```
from crazyshit import db
```

Secord, create the database with this command:

```
db.create_all()
```

### Run server

With this command:

```
(venv) $ export FLASK_APP=app.py
(venv) $ export PYTHONPATH=/Path/to/the/app
(venv) $ flask run
```

### In Browser

Paste this url and hit enter:

```
http://localhost:5000/
```

### Tests

You can run the tests with this command:

```
(venv) $ python3 api/test_views.py
```

### How I decided what tests to write

I decided for the API integration tests because they test the overall functionality of the API endpoint (error messages, response codes, headers...). This is very important aspect for RESTful design architecture.

**Integration tests**:

I write the integration tests in this order:

**POST - GET - GET:id - PUT - DELETE.**

For each HTTP method, I start with as little functionality as possible.
I write the integration tests for each HTTP method in this order:

- test for creating a user without authentication
- test for creating a user with authentication
- other edge cases

What response code the test returns does not influence my decision in which order I write an integration test. This way, I make sure that all test cases are covered.

### REST API Architecture

- **GET user/** – Retrieves list of users
(authentication necessary)
- **GET user/<public_id>** – Retrieves the one users details of the <public_id>
(authentication necessary)
- **POST user/** – Create a new user without authentication
- **DELETE user/<public_id>** – Delete the user of the <public_id>
(authentication necessary)
- **PUT tasks/<public_id>** – Update the user of the <public_id>
(authentication necessary)

