from flask import Flask, render_template, jsonify, request
import psycopg2
import json

app = Flask(__name__)

database = 'test-db'
user = 'postgres'
password = 'postgres'
host = 'localhost'
port = 5432

# Establish the connection
connection = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

# Open a cursor to perform database operations
cursor = connection.cursor()

# Execute a test query
cursor.execute("SELECT * FROM campus;")

# Retrieve query results
records = cursor.fetchall()

# Check if there are any tables
if not records:
    print("No tables found in the database.")
else:
    for name in records:
        print(name)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/index')
def index():
    return render_template('index.html', mycontent=records)


@app.route('/test-api', methods=['GET'])
def getCampusName():
    return jsonify(records)
