from flask import Flask, request
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)

class PersonResource(Resource):
    def post(self):
        data = request.get_json(force=True)
        print("Received data:", data)
        if data:
            # Read the existing data from the file
            with open("person.json", "r") as json_file:
                existing_data = json.load(json_file)
            
            # Append the new person's data to the list of persons
            existing_data["person"].append(data)

            # Write the updated data back to the file
            with open("person.json", "w") as json_file:
                json.dump(existing_data, json_file)
            
            return {"message": "Data saved"}, 201
        else:
            return {"message": "Invalid Data"}, 400

api.add_resource(PersonResource, '/person')

# this is how to start the server in python
if __name__ == "__main__":
    app.run(debug=True)
