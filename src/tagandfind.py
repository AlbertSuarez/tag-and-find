from flask import Flask, render_template, request
from flask_cors import CORS

from src.nlp.sort import sort_places


app = Flask(__name__, template_folder='templates/')
CORS(app)


@app.route('/')
def render_static():
    return render_template('tag.html')


@app.route('/search')
def search():
    # Get params
    location = request.args.get('location')
    necessity = request.args.get('necessity')
    features = request.args.get('features')

    # Sort places
    response = sort_places(location, necessity, features.split('_'))
    return response
