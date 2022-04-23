# manage-places

# Task
Assigned to build a To-do app API with these features:
- Register user 
- Login user
- User can create a task
- User can view all the tasks
- User can categorize tasks (add task into a group)
- List all user


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
$ cd todo_app
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

- Project will be running on 127.0.0.1:8000


## Endpoints
API Endpoints:

- /api                   GET                => shows all places created in the database
- /api                   POST               => create a new place
- /api/<slug>            GET               => retrieve a specific place by slug
- /api/<slug>            POST               => update details of a specific place by slug
- /api/<slug>            DELETE             => delete a specif place
- /admin                 POST               => admin panel (create a super user to login as admin)