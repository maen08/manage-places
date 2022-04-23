# manage-places

# Task
- Create a CRUP API for managing places
- Create testing environment (I chose to use docker)
- Document the API in the README file
- Structure, Clean and readable codes
- VCs good practices


## Run the project with Docker (Recommended)
- The project is dockerized and shipped on the docker hub as an independent docker container. To run this container follow this steps (make sure you have docker installed in your machine):

```
# Pull the container from the dockerhub (registry)
docker pull maen08/manage_places

# Run the container
docker run -d manage_places

# Navigate to your web browser, the link should be
# http://YOUR_IP_ADDRESS:8000/api

```


## Run the project Manually (Optional)
- Clone a repo and install all dependencies
```
$ git clone https://github.com/maen08/Simple_Task.git

$ cd Simple_Task

$ pip install -r requirements.txt 
```

## Run the project
```
# Navigate to root directory of the project (make sure you see manage.py file)
$ cd manage_places
$ cd manage_place_project

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