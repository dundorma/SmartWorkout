from dotenv import load_dotenv

from flask import Flask, request, redirect
from flask_restful import Resource, Api
from flask_cors import CORS
import os

load_dotenv()

app = Flask(__name__)
# cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

class HomePage(Resource):
    def get(self):
        return 'Welcome to, API HomePage!'

    def post(self):
        try:
            value = request.get_json()
            if(value):
                return {'Post Values': value}, 201

            return {"error":"Invalid format."}

        except Exception as error:
            return {'error': error}

class RecommendationFeedback(Resource):
    def get(self):
        return {"error":"Invalid Method."}

    def post(self):
        try:
            return {}

        except Exception as error:
            return {'error': error}

class Counter(Resource):
    def get(self):
        return {"error":"Invalid Method."}

    def post(self):
        try:
            return {}

        except Exception as error:
            return {'error': error}


ROOT_PATH = os.getenv('API_ROOT_PATH')
api.add_resource(HomePage,'/')
api.add_resource(Counter,f'{ROOT_PATH}/workout_counter')
api.add_resource(RecommendationFeedback,f'{ROOT_PATH}/recommendation')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
    