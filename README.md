# manage-places

# Task
- Create a CRUP API for managing places
- Create testing environment (I chose to use docker)
- Document the API in the README file
- Structure, Clean and readable codes
- VCs good practices


## Base endpoint

- http://0.0.0.0:8000/api


## Run the project with Docker (Recommended)
- The project is dockerized in a container with the help of docker and docker-compose

(make sure you have docker and docker-compose installed in your machine):

```
# Clone the project
git clone https://github.com/maen08/manage-places.git

# Navigate to the directory
cd manage_place_project

# make sure you're in the directory where you see manage.py file (when you list eg. ls) 

# Run the container
docker-compose up --build


# Navigate to your web browser, the link should be
# http://0.0.0.0:8000/api

```


## Run the project Manually (Optional)
- Clone a repo and install all dependencies
```
$ git clone https://github.com/maen08/manage-places.git

$ cd manage_place_project

$ pip install -r requirements.txt 


# Navigate to root directory of the project (make sure you see manage.py file)


# Prepare the database by running
$ python manage.py makemigrations

# Make changes in the database
$ python manage.py migrate

# Run the server
$ python manage.py runserver
```

- Project will be running on 127.0.0.1:8000


## Endpoints
API Endpoints:

- /api                   GET                => shows all places created in the database
- /api                   POST               => create a new place
- /api/<slug>            GET                => retrieve a specific place by slug
- /api/<slug>            POST               => update details of a specific place by slug
- /api/<slug>            DELETE             => delete a specif place
- /admin                 POST               => admin panel (create a super user to login as admin)


## Testing API
- You can test these API using any tool of your choice for exaple:
    - Postman
    - ThunderClient



# By
- [maen08](https://github.com/maen08)