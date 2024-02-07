import sqlite3
from sql_queries import create_database, test_data, select_photographers
from sql_queries import select_customers, select_jobs, select_students_grades
from sql_queries import select_students_parents, select_orders_by_customer, select_price_sheets
from sql_queries import select_barcodes_students, select_orders_revenue, select_all_jobs_school




class DatabaseConnector:
    def __init__(self, db_name="example.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)

    def execute_query(self, query, params=None):
        """ Execute a query on the database. """
        with self.connection:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()

    def create_table(self, table_query):
        """ Create a table in the database. """
        try:
            self.execute_query(table_query)
        except:
            print("Table may already exist")

    def insert_data(self, insert_query):
        """ Insert data into the table. """
        try:
            self.execute_query(insert_query)
        except:
            print("Data may already exist")
    def close(self):
        """ Close the database connection. """
        self.connection.close()

# Example usage:

# Initialize the database connector
db = DatabaseConnector("my_database.db")



for i in create_database:
  db.create_table(i)


for i in test_data:
  db.insert_data(i)

x = db.execute_query(select_orders_revenue)
for i in x:
    print(i)
# Insert some data
#insert_query = "INSERT INTO users (name, age) VALUES (?, ?)"
#db.insert_data(insert_query, ("Alice", 30))
#db.insert_data(insert_query, ("Bob", 25))

## Query the database
#select_query = "SELECT * FROM users"
#users = db.execute_query(select_query)
#for user in users:
#    print(user)

# Close the connection
db.close()
