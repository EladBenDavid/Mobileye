import clickhouse_connect
import json


class ClickhouseAdapter:

    # Constructor to initialize the object with connection details and query templates
    def __init__(self, hostname, port, user, password):
        self.hostname = hostname
        self.password = password
        self.user = user
        self.port = port

        # Load the SQL query templates
        self.insert_vehicles_status = load_query('insert_vehicles_status.sql')
        self.insert_objects_detection = load_query('insert_objects_detection.sql')

    # Method to connect to the ClickHouse server
    def connect(self):
        self.client = clickhouse_connect.get_client(host=self.hostname,
                                                    port=self.port, username=self.user, password=self.password)

    # Method to initialize the necessary database and tables
    def db_init(self):
        # Load and execute the SQL query to create the database
        create_db = load_query('create_db.sql')
        self.client.command(create_db)

        # Load and execute the SQL query to set the required settings
        settings = load_query('settings.sql')
        self.client.command(settings)

        # Load and execute the SQL query to create the 'vehicles_status' table
        create_vehicles_status_table = load_query('create_vehicles_status_table.sql')
        self.client.command(create_vehicles_status_table)
        print("Table 'create_vehicles_status_table' created or already exists!")

        # Load and execute the SQL query to create the 'objects_detection' table
        create_objects_detection_table = load_query('create_objects_detection_table.sql')
        self.client.command(create_objects_detection_table)
        print("Table 'create_objects_detection_table' created or already exists!")

    # Method to add vehicle status data to the 'vehicles_status' table
    def add_vehicle_status(self, data):
        # Execute the SQL query to insert vehicle status data into the table
        self.client.query(self.insert_vehicles_status + json.dumps(data))
        print(f"Written 'vehicles_status' data: {data}")

    # Method to add objects detection data to the 'objects_detection' table
    def add_objects_detection(self, data):
        # Execute the SQL query to insert objects detection data into the table
        self.client.query(self.insert_objects_detection + json.dumps(data))
        print(f"Written into 'objects_detection': {data}")


# Function to load SQL queries from files
def load_query(file):
    fd = open(f'db/{file}', 'r')
    sql_file = fd.read()
    fd.close()
    return sql_file
