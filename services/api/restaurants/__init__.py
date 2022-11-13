from flask import Flask, jsonify
import os
from postgres import Postgres

app = Flask(__name__)

DATABASE_URL = os.environ.get('DATABASE_URL')
connection = Postgres(DATABASE_URL)


@app.route('/locations')
def locations():
    locations = connection.all('SELECT * FROM locations;')
    return jsonify({'locations': locations})
