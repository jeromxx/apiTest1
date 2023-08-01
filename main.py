from flask import Flask
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)

class PersonResource(Resource):
    def post(self):
        data = request.get_json()
        if data:
            with open("person.json", w) as json_file:
                json.dump(data, json_file)
            return {"message": "Data saved"}, 201
        else:
            return {"message": "Invalid Data"},400

api.add_resource(PersonResource, '/person')

# this is how to start the server in python
if __name__ == "__main__":
    app.run(debug=True) 
