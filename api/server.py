# This is the key file for the described folder setup
# This file contains the app and routes. You would also this file to setup config values
# such as (before_request(), after_request())... basically this file configures the application

from flask import Flask
from flask_restful import Api
from api.resources.comment import Comment
from api.resources.sentiment import Sentiment

app = Flask(__name__)
server = Api(app)


# setup routes
server.add_resource(Comment, "/comment", "/comment/<string:video_id>")
server.add_resource(Sentiment, "/sentiment/<string:video_id>")
