import psycopg2

# Connection parameters
database = "moduledb"
user = "postgres"
password = "postgres"
host = "localhost"  # or "127.0.0.1"
port = 5432  # or the local port used in the SSH tunnel

# Establish the connection
conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a test query
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")

# Retrieve query results
records = cur.fetchall()

# Check if there are any tables
if not records:
    print("No tables found in the database.")
else:
    print("Tables in the database:")
    for table in records:
        print(table[0])

# # Finally, you may print the output to the console or use it anyway you like
# print(records)