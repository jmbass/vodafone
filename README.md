## Vodafone Python test

Vodafone's test consist on five simple questions and tasks. For each question, there's a .py and a .txt file available.

The txt file will cover up the theorical answer and the Python scripts will serve as a proof of concept.

The fifth question consist in a task where it is required to develop a simple API that populates a database on initialization. For this purpose, Flask is used.

The chosen Database for this matter is MongoDB, as it is more comfortable to insert mongo documents as JSON objects retrieved from the JSONplaceholder API.

A relational database could also be used, but that'd require to create several tables and foreign references in order to store the objects adequately.

MongoDB is required. Please install it from their official site or, if Docker is installed, you can easily run a MongoDB container with the following command in this project's root directory :dancer: :

```sh
$ docker-compose up --build
```

It will expose MongoDB at the port 27017, so please keep that in mind if you prefer to install it manually. For simplicity reasons, the question_5.py flask app will connect to mongo through localhost and this is hard-coded, but feel free to change it.

This Flask app could also be dockerized, but I reckon that you want to see the installation. 

To install all the dependencies needed, please run the following command:

```sh
$ pip install --no-index --find-links=./wheel/ -r requirements.txt
```

After that, you can run the app with:

```sh
$ python question_5.py
```
Please take into account that this project needs Python 3.x, so if you're on MacOS as I am, you should use these commands in order to start the API:

```sh
$ pip3 install --no-index --find-links=./wheel/ -r requirements.txt
$ python3 question_5.py
```


It will listen through port 5000. Let's see the API reference:

## API reference

**Users**

```sh
REQUEST::
curl -X GET \
  http://localhost:5000/users \
  -H 'content-type: application/json'
```
```sh
RESPONSE::
[
  {
    "_id": "int",
    "name": "string",
    "username": "string",
    "email": "string",
    "address": {
      "street": "string",
      "suite": "string",
      "city": "string",
      "zipcode": "string",
      "geo": {
        "lat": "float",
        "lng": "float"
      }
    },
    "phone": "string",
    "website": "string",
    "company": {
      "name": "string",
      "catchPhrase": "string",
      "bs": "string"
    }
  }


  ....
]
```

It was asked to provide a function so a user info can be retrieved with it's user ID

```sh
REQUEST::
curl -X GET \
  http://localhost:5000/users/<int:id> \
  -H 'content-type: application/json'
```
```sh
RESPONSE::
  {
    "_id": "int",
    "name": "string",
    "username": "string",
    "email": "string",
    "address": {
      "street": "string",
      "suite": "string",
      "city": "string",
      "zipcode": "string",
      "geo": {
        "lat": "float",
        "lng": "float"
      }
    },
    "phone": "string",
    "website": "string",
    "company": {
      "name": "string",
      "catchPhrase": "string",
      "bs": "string"
    }
  }
```

** Posts **

Return all posts from the same user:

```sh
REQUEST::
curl -X GET \
  http://localhost:5000/users/<int:id>/posts \
  -H 'content-type: application/json'
```
```sh
RESPONSE::
[
  
    "_id": "int",
    "userId": "int",
    "title": "string",
    "body": "string"
  }
...
]
```

Return particular posts and their comments:
** Posts **

Return all posts from the same user:

```sh
REQUEST::

curl -X GET \
  http://localhost:5000/posts/<int:id> \
  -H 'content-type: application/json'
```
```sh
RESPONSE::

  {
  "_id": "int",
  "userId": "int",
  "title": "string",
  "body": "string",
  "comments": [
    {
      "_id": "int",
      "postId": "int",
      "name": "string",
      "email": "string",
      "body": "string"
    }
  }

  ...
  ]
```

There are more endpoints :smile: please check out the question_5.py comments for more details.




