# 5. Write a python program following the requirements below:
# The program must retrieve, on startup, the users, the first 10 posts (sorted by ID) and the comments of
# those posts from https://jsonplaceholder.typicode.com/ API (see the link to get all the information)
# The data, had not been written before, shall be stored in a DB
# The program will expose an API with the following functions:
# Return info from a userID
# Return all posts from the same user
# Return a particular post and its comments
# The code shall include the means to generate a pip wheel to be installed in any target machine by pip,
# including installing a script to call the program from the CLI, alongside a small README file with the
# necessary instructions

import flask

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello, there</h1><p>I'm here</p>"

app.run()


