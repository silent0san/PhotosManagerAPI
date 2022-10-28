# PhotosManagerAPI

---
## Functionalities: 

1. Photos REST management (list, create, update, delete).
2. Importing photos from External API and JSON files using REST API and CLI scripts.
3. Implemented testing for models, serializers, views.
---
## About app
This app is using:
- Python 3.8.15
- Django 4.0.3
- Django Rest Framework 3.13.1

It is required in order to run project to use Docker and Docker-Compose.

In order to run this app use **bash script** in root project directory:

---
## To build: 
`./build.sh -b`
## To clean up:
`./build.sh -d`

In order to use API please log in using: `http://127.0.0.1:8000/admin/` with generated user credentials: 
Username: `testadmin`, Password: `test123`

In order to use API please use: `http://localhost:8000/api/` 

For detailed object view: `http://127.0.0.1:8000/api/{uuid}`

---
## Connection to docker container

In order to send requests please use CLI to connect to docker container: 

Please use `docker ps` to get Container ID.

![alt text](https://i.imgur.com/ac9Ooay.png)

Use Container ID to connect to docker container:
`winpty docker exec -it d4ed1c688435 bash` 

**(winpty is required for windows)** 

**(bash is optional for Git Bash)**

![alt text](https://i.imgur.com/iTVbpU9.png)

Once the connection is established user is able to send requests.

---
# Sending requests

## Import photos from JSON using REST API
```
curl --location --request POST 'http://127.0.0.1:8000/api/import_from_json/' \
--header 'Authorization: Basic dGVzdF9hZG1pbjp0ZXN0MTIz' \
--header 'Content-Type: application/json' \
--data-raw '[
    {
        "albumId": 5000,
        "title": "Json Example 1",
        "url": "https://via.placeholder.com/600/92c952"
    },
    {
        "albumId": 5001,
        "title": "Json Example 2",
        "url": "https://via.placeholder.com/600/51aa97"
    }
]'
```
## Import photos from external API
```
curl --location --request POST 'http://127.0.0.1:8000/api/import_from_url/' \
--header 'Authorization: Basic dGVzdF9hZG1pbjp0ZXN0MTIz' \
--header 'Content-Type: application/json' \
--data-raw '{
    "api_url": "https://jsonplaceholder.typicode.com/photos"
}'
```


## Import photos from JSON file using CLI script
In order to import photos using CLI script please connect to Docker Container and use command:

`python manage.py import_from_json Sample_Json_Data`

## Import photos from external API using CLI script
In order to import photos from external API using CLI script please connect to Docker Container and use command:

`python manage.py import_from_api 'https://jsonplaceholder.typicode.com/photos'`

> Important: **Loading whole data from URL can take some time.**

---
# Tests
In order to test application please connect to Docker container and use command:
`python manage.py test`


>**For Windows users it is recommended to use Git Bash.**
