from email import message
from flask import Flask
from flask_restful import Api, Resource, abort, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from requests import request
from flask_sqlalchemy import SQLAlchemy


# Defining app

app  = Flask(__name__)
# Wrap an app in an API
api = Api(app)
app.config['SWLALCHEMY_DATABASE_URI'] = 'sqllite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name={name}, views={views}, likes={likes})"


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is a required field", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True)
# If valid argument is not correct

resource_fields = {
    "id":fields.Integer,
    "name":fields.String,
    "views":fields.Integer,
    "likes":fields.Integer

}


names = {"tim":{"age":19, "gender": "male"},
        "lawe":{"age":20,"gender":"male"}
        }




class Video(Resource):

    # When we return take these fields and serialize them into json format
    @marshal_with(resource_fields)
    
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Could not find video with that id")
        return result

    @marshal_with(resource_fields)

    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(409, message="Sorry that ID is taken")
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])

        db.session.add(video)
        db.session.commit()
        return video,201

    @marshal_with(resource_fields)

    def delete(self, video_id):
        absent_video_id(video_id)
        del videos[video_id]
        return '',204

api.add_resource(Video,"/video/<int:video_id>")


# class HelloWorld(Resource):
#     # Get request
#     def get(self, name):
#         return names[name]
#     # Post request
#     def post(self):
#         return{"data":"posted"}

# # Registering this as a resource

# # Using parameters
# api.add_resource(HelloWorld,"/helloworld/<string:name>")

if __name__ =="__main__":
    app.run(debug=True)
