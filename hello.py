from flask import Flask, render_template, jsonify, request
import configparser
import psycopg2
import json

app = Flask(__name__)
app.json.sort_keys = False

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the file using the object
config.read('config.ini')

# Obtain the configuration values
database = config.get('database', 'database')
user = config.get('database', 'user')
password = config.get('database', 'password')
host = config.get('database', 'host')
port = config.get('database', 'port')

# Establish the connection
connection = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

# Open a cursor to perform database operations
cursor = connection.cursor()

# Execute a test query
cursor.execute("SELECT * FROM campus;")

# Retrieve query results
records = cursor.fetchall()

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/sample-table')
def index():
    return render_template('sample-table-api.html')


@app.route('/getAllData', methods=['GET'])
def getAllData():
    # Get column names from cursor description
    column_names = [desc[0] for desc in cursor.description]

    # Build a list of dictionaries with column headers and values
    result_data = []
    for row in records:
        result_data.append(dict(zip(column_names, row)))

    return jsonify(result_data)
