from flask_pymongo import PyMongo
import requests

def intialize(mongo):

    # The JSONplaceholder API it's already returining objects as required
    print("Initializing Database...")
    if 'users' not in mongo.db.list_collection_names():
        users = requests.get("https://jsonplaceholder.typicode.com/users").json()
        for user in users:
            user['_id'] = user.pop('id')
        print('Loading users')
        mongo.db.users.insert_many(users)
    if 'posts' not in mongo.db.list_collection_names():
        posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()
        for post in posts:
            post['_id'] = post.pop('id')
        print('Loading comments...')
        mongo.db.posts.insert_many(posts)
    if 'comments' not in mongo.db.list_collection_names():
        comments = requests.get("https://jsonplaceholder.typicode.com/comments").json()
        for comment in comments:
            comment['_id'] = comment.pop('id')
        print('Loading posts...')
        mongo.db.comments.insert_many(comments)
    

    # Let's override the default _id
    
    #I'm assuming that what must be retrieved are the first 10 posts of each user.
    
    
    
    