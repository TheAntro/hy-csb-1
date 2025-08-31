# Installation

The project does not have additional requirements in addition to what comes installed with Django.
If you already have Django installed globally on your machine, simply run the following commands to start the server:

```
cd csb1
python manage.py migrate
python manage.py runserver
```

Then proceed to localhost:8000/faultyweb. You can follow the links on the top of the page to navigate on the page.

Start by registering via Register page, and the Login with the credentials you just created.

## Installation with a separate virtual environment

First create a virtual environment

```
python -m venv venv
```

Then activate the virtual environment

```
// on Windows:
venv\Scripts\activate

// On Linux/macos:
source venv/bin/activate
```

Then install dependencies:

```
pip install -r requirements.txt
```

Then run the following commands to start the server:

```
cd csb1
python manage.py migrate
python manage.py runserver
```
