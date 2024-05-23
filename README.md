# Getting Started:

### Clone this repo:

`$ git clone https://github.com/JipVeerbeek/Simple-Configurator.git`

### Create .venv:

`$ python3 -m venv .venv`

### Activate .venv:

`$ source .venv/bin/activate`

### Go to project folder:

`$ cd simple_configurator`

### Install requirements:

`$ pip install -r requirements.txt`

### Start your container:

`$ docker compose up --build`

# After Installation:

### Run Migrations:
***Initializes your database.***

`docker compose exec web ./manage.py migrate`

### Load Fixtures:
***Adds dummydata to you database.***

`docker compose exec web ./manage.py load_dynamic_fixtures`

### Run Tests
***Tests the endpoints.***

`docker compose exec web ./manage.py test`

### Swagger:
***Allows you to try out endpoints***

`http://localhost:8000/api/swagger/`

### Django Admin:
***The build in database viewer.***

`http://localhost:8000/admin/`
