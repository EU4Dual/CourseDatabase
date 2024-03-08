import configparser
import psycopg2
import openpyxl

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
cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")

# Retrieve query results
records = cursor.fetchall()

# Check if there are any tables
if not records:
    print("No tables found in the database.")
else:
    print("Tables in the database:")
    for table in records:
        print(table[0])

# # Finally, you may print the output to the console or use it anyway you like
# print(records)