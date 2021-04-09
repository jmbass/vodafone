print('''
5. Write a python program following the requirements below:
The program must retrieve, on startup, the users, the first 10 posts (sorted by ID) and the comments of
those posts from https://jsonplaceholder.typicode.com/ API (see the link to get all the information)
The data, had not been written before, shall be stored in a DB
The program will expose an API with the following functions:
Return info from a userID
Return all posts from the same user
Return a particular post and its comments
The code shall include the means to generate a pip wheel to be installed in any target machine by pip,
including installing a script to call the program from the CLI, alongside a small README file with the
necessary instructions
''')

from flask import Flask, Response, request
from bson import json_util
import requests
import json
import persistence
from flask_pymongo import PyMongo
import pymongo

def page_not_found(e):
  return {}, 404

app = Flask(__name__)
app.config['MONGO_URI'] =  'mongodb://localhost:27017/vodafone'
app.register_error_handler(404, page_not_found)
# Init DB if it hasn't yet

mongo = PyMongo(app)

persistence.intialize(mongo)

# Returns all users
@app.route('/users', methods=['GET'])
def show_all_users():
    return Response(json_util.dumps(mongo.db.users.find()), mimetype="application/json")

#  Returns specific user
@app.route('/users/<int:userId>', methods=['GET'])
def show_user(userId):
    return Response(json_util.dumps(mongo.db.users.find_one(userId)), mimetype="application/json")

# Returns specific user's posts
@app.route('/users/<int:userId>/posts', methods=['GET'])
def show_user_posts(userId):
    return Response(json_util.dumps(mongo.db.posts.find_one({'userId': int(userId)})), mimetype="application/json")

# returns specific user posts (or all of them) with query parameters
@app.route('/posts', methods=['GET'])
def show_posts_from_users():
    userId = request.args.get('userId')
    return Response(json_util.dumps(mongo.db.posts.find({'userId': int(userId)}).sort('_id', pymongo.DESCENDING)), mimetype="application/json") if userId is not None else Response(json_util.dumps(mongo.db.posts.find().sort('_id', pymongo.DESCENDING)), mimetype="application/json")

# returns specific post with its comments
@app.route('/posts/<int:id>', methods=['GET'])
def show_post(id):
    post = mongo.db.posts.find_one(id)
    post['comments']  = mongo.db.comments.find({'postId': int(id)})
    return Response(json_util.dumps(post), mimetype="application/json")

# returns a specific post comments
@app.route('/posts/<int:postId>/comments', methods=['GET'])
def show_post_comments(postId):
    return Response(json_util.dumps(mongo.db.comments.find({'postId': int(postId)})), mimetype="application/json")

# returns comments of a specific post with query parameters
@app.route('/comments', methods=['GET'])
def show_comments_from_post():
    postId = request.args.get('postId')
    return Response(json_util.dumps(mongo.db.comments.find({'postId': int(postId)})), mimetype="application/json") if postId is not None else Response(json_util.dumps(mongo.db.comments.find()), mimetype="application/json")



app.run()


