from modules.llm import openai_chat
from dotenv import load_dotenv

from flask import Flask, request, redirect, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import os

load_dotenv()

app = Flask(__name__)
# cors = CORS(app, resources={r"*": {"origins": "*"}})
# api = Api(app)
ROOT_PATH = os.getenv('API_ROOT_PATH')

@app.route("/")
def index():
    return 'Welcome to, API HomePage!'


@app.route(f'{ROOT_PATH}/recommendation', methods=["GET", "POST"])
def RecommendationFeedback():
    message = request.json.get("message")
    print(message)
    response = openai_chat(message, model='llama3-8b-8192')
    print(response)
    return {'response':response}

@app.route(f'{ROOT_PATH}/workout_counter', methods=["POST"])
def Counter():
    return {"error":"Invalid Method."}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
    