import os
import sqlite3
import csv
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from datetime import datetime
import time
import shutil

# Get the current working directory
current_directory = os.getcwd()

# Define the directory name to be deleted
directory_to_delete = "plots"

# Construct the full path to the directory
directory_path = os.path.join(current_directory, directory_to_delete)

# Check if the directory exists before attempting to delete it
if os.path.exists(directory_path) and os.path.isdir(directory_path):
    # Use try-except to handle any potential errors during deletion
    try:
        # Remove the directory and its contents (recursively)
        shutil.rmtree(directory_path)
        print(f"Directory '{directory_to_delete}' and its contents have been successfully deleted.")
    except Exception as e:
        print(f"An error occurred while deleting the directory: {str(e)}")
else:
    print(f"Directory '{directory_to_delete}' does not exist.")

def MakeProcessing():
    # Delete the existing processing.db file if it exists
    if os.path.exists('processing.db'):
        os.remove('processing.db')

    # Connect to the source database
    with sqlite3.connect('prance.db') as source_conn:
        source_cursor = source_conn.cursor()

        # Connect to the new database or create it
        with sqlite3.connect('processing.db') as target_conn:
            target_cursor = target_conn.cursor()

            # Retrieve unique lagoon numbers from the source database
            source_cursor.execute("SELECT DISTINCT lagoon_number FROM measurements")
            lagoon_numbers = [row[0] for row in source_cursor.fetchall()]

            # Loop through lagoon numbers
            for lagoon_number in lagoon_numbers:
                # Create the new table in the target database
                create_table_query = f'''
                CREATE TABLE IF NOT EXISTS lagoon_{lagoon_number} (
                    id INTEGER PRIMARY KEY,
                    GFP REAL,
                    lum REAL,
                    abs REAL,
                    measurementtime REAL,
                    inoculated REAL,
                    bacteria_id REAL
                )
                '''
                target_cursor.execute(create_table_query)

                # Retrieve readings and timestamps for the current lagoon number from the source database
                source_cursor.execute("SELECT reading, timestamp, inoculated, bacteria_id FROM measurements WHERE lagoon_number = ?", (lagoon_number,))
                data_entries = source_cursor.fetchall()
                #print (data_entries)
                # Convert initial measurementtime to a datetime object
                initial_measurementtime = datetime.strptime(data_entries[0][1], '%Y-%m-%d %H:%M:%S.%f')
                
                # Insert interleaved readings and adjusted measurementtime (in hours) into the target database
                for i in range(0, len(data_entries), 3):
                    gfp = data_entries[i][0]
                    lum = data_entries[i+1][0]
                    abs_value = data_entries[i+2][0]
                    inoculated = data_entries[i][2]
                    bacteria_id = data_entries[i][3]
                    adjusted_time = (datetime.strptime(data_entries[i][1], '%Y-%m-%d %H:%M:%S.%f') - initial_measurementtime).total_seconds() / 3600.0
                    
                    
                    insert_query = f'''
                    INSERT INTO lagoon_{lagoon_number} (GFP, lum, abs, measurementtime, inoculated, bacteria_id)
                    VALUES (?, ?, ?, ?, ?,?)
                    '''
                    target_cursor.execute(insert_query, (gfp, lum, abs_value, adjusted_time, inoculated, bacteria_id))
                
            # Commit the changes after processing all lagoon numbers
            target_conn.commit()

    # Cursors and connections are automatically closed when exiting the context managers

# Call the function to execute the processing

MakeProcessing()


def delete_processing2_db_file():
    file_path_0 = "processing 2_0.db"
    file_path_1 = "processing 2_1.db"
    file_path_2 = "processing 2_2.db"

    if os.path.exists(file_path_0):
        os.remove(file_path_0)
        print(f"{file_path_0} has been deleted.")
    else:
        print(f"{file_path_0} not found. No action taken.")
    if os.path.exists(file_path_1):
        os.remove(file_path_1)
        print(f"{file_path_1} has been deleted.")
    else:
        print(f"{file_path_1} not found. No action taken.")
    if os.path.exists(file_path_2):
        os.remove(file_path_2)
        print(f"{file_path_2} has been deleted.")
    else:
        print(f"{file_path_2} not found. No action taken.")

# Call the function to delete the file if it exists, or do nothing if it doesn't.
delete_processing2_db_file()



def open_processing_database():
  """Opens the processing database in the same directory as this file."""
  import sqlite3

  # Get the current working directory
  current_directory = os.getcwd()

  # Create the database file path
  database_file_path = os.path.join(current_directory, "processing.db")

  # Open the database connection
  connection = sqlite3.connect(database_file_path)

  # Return the connection object
  return connection

connection = open_processing_database()


#filling out the sql worksapce bacteria 1


def append_data_to_new_table(connection):
  """Appends all data from columns 2 3 4 and 5 of tables where value in column 7 is 0 to a new table titled bacteria 0 in a new sql database called processing 2."""
  # Get the list of tables in the database
  tables = connection.execute("SELECT name FROM sqlite_master WHERE type='table';")

  # Create a new database called processing 2
  processing_2_connection = sqlite3.connect("processing 2_0.db")

  # Create a new table called bacteria 0
  processing_2_connection.execute("CREATE TABLE bacteria_0 (column2 TEXT, column3 TEXT, column4 TEXT, column5 TEXT, column6 TEXT);")

  # Iterate over the tables
  for table in tables:
    table_name = table[0]

    # Get the data from the table where value in column 7 is 0
    data = connection.execute(f"SELECT GFP, lum, abs, measurementtime, inoculated FROM {table_name} WHERE bacteria_id = 0;")

    # Iterate over the data
    for row in data:
      # Insert the data into the new table
      processing_2_connection.execute(f"INSERT INTO bacteria_0 (column2, column3, column4, column5, column6) VALUES ('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}');")
      
  # Commit the changes to the new database
  processing_2_connection.commit()
  
  

  # Close the database connections
  connection.close()
  processing_2_connection.close()

connection = open_processing_database()
append_data_to_new_table(connection)

def append_data_to_new_table(connection):
  """Appends all data from columns 2 3 4 and 5 of tables where value in column 7 is 0 to a new table titled bacteria 0 in a new sql database called processing 2."""
  # Get the list of tables in the database
  tables = connection.execute("SELECT name FROM sqlite_master WHERE type='table';")

  # Create a new database called processing 2
  processing_2_connection = sqlite3.connect("processing 2_1.db")

  # Create a new table called bacteria 0
  processing_2_connection.execute("CREATE TABLE bacteria_1 (column2 TEXT, column3 TEXT, column4 TEXT, column5 TEXT, column6 TEXT);")

  # Iterate over the tables
  for table in tables:
    table_name = table[0]

    # Get the data from the table where value in column 7 is 0
    data = connection.execute(f"SELECT GFP, lum, abs, measurementtime, inoculated FROM {table_name} WHERE bacteria_id = 1;")

    # Iterate over the data
    for row in data:
      # Insert the data into the new table
      processing_2_connection.execute(f"INSERT INTO bacteria_1 (column2, column3, column4, column5, column6) VALUES ('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}');")
      
  # Commit the changes to the new database
  processing_2_connection.commit()
  
  

  # Close the database connections
  connection.close()
  processing_2_connection.close()

connection = open_processing_database()
append_data_to_new_table(connection)

def append_data_to_new_table(connection):
  """Appends all data from columns 2 3 4 and 5 of tables where value in column 7 is 0 to a new table titled bacteria 0 in a new sql database called processing 2."""
  # Get the list of tables in the database
  tables = connection.execute("SELECT name FROM sqlite_master WHERE type='table';")

  # Create a new database called processing 2
  processing_2_connection = sqlite3.connect("processing 2_2.db")

  # Create a new table called bacteria 0
  processing_2_connection.execute("CREATE TABLE bacteria_2 (column2 TEXT, column3 TEXT, column4 TEXT, column5 TEXT, column6 TEXT);")

  # Iterate over the tables
  for table in tables:
    table_name = table[0]

    # Get the data from the table where value in column 7 is 0
    data = connection.execute(f"SELECT GFP, lum, abs, measurementtime, inoculated FROM {table_name} WHERE bacteria_id = 2;")

    # Iterate over the data
    for row in data:
      # Insert the data into the new table
      processing_2_connection.execute(f"INSERT INTO bacteria_2 (column2, column3, column4, column5, column6) VALUES ('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}');")
      
  # Commit the changes to the new database
  processing_2_connection.commit()
  
  

  # Close the database connections
  connection.close()
  processing_2_connection.close()

connection = open_processing_database()
append_data_to_new_table(connection)



## next is the bit to move the time data to the left


# Connect to the database
conn = sqlite3.connect('processing 2_0.db')
cursor = conn.cursor()

# Get a list of tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Iterate through each table
for table in tables:
    table_name = table[0]
    
    # Get the list of column names in the table
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    column_names = [column[1] for column in columns]
    
    # Ensure there are at least 4 columns
    if len(column_names) >= 4:
        # Swap the positions of columns 1 and 4, and shift others to the right
        column1_name = column_names[0]
        column4_name = column_names[3]
        other_columns = ", ".join(column_names[1:3] + column_names[4:])
        
        # Create a new table with the modified column order and preserve data from column 1
        create_table_sql = f"CREATE TABLE {table_name}_new AS SELECT {column4_name}, {other_columns}, {column1_name} AS temp_column FROM {table_name};"
        
        cursor.execute(create_table_sql)
        
        # Drop the old table
        cursor.execute(f"DROP TABLE {table_name};")
        
        # Rename the new table to the original table name
        cursor.execute(f"ALTER TABLE {table_name}_new RENAME TO {table_name};")

# Commit the changes and close the connection
conn.commit()
conn.close()

# Connect to the database
conn = sqlite3.connect('processing 2_1.db')
cursor = conn.cursor()

# Get a list of tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Iterate through each table
for table in tables:
    table_name = table[0]
    
    # Get the list of column names in the table
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    column_names = [column[1] for column in columns]
    
    # Ensure there are at least 4 columns
    if len(column_names) >= 4:
        # Swap the positions of columns 1 and 4, and shift others to the right
        column1_name = column_names[0]
        column4_name = column_names[3]
        other_columns = ", ".join(column_names[1:3] + column_names[4:])
        
        # Create a new table with the modified column order and preserve data from column 1
        create_table_sql = f"CREATE TABLE {table_name}_new AS SELECT {column4_name}, {other_columns}, {column1_name} AS temp_column FROM {table_name};"
        
        cursor.execute(create_table_sql)
        
        # Drop the old table
        cursor.execute(f"DROP TABLE {table_name};")
        
        # Rename the new table to the original table name
        cursor.execute(f"ALTER TABLE {table_name}_new RENAME TO {table_name};")

# Commit the changes and close the connection
conn.commit()
conn.close()

# Connect to the database
conn = sqlite3.connect('processing 2_2.db')
cursor = conn.cursor()

# Get a list of tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Iterate through each table
for table in tables:
    table_name = table[0]
    
    # Get the list of column names in the table
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    column_names = [column[1] for column in columns]
    
    # Ensure there are at least 4 columns
    if len(column_names) >= 4:
        # Swap the positions of columns 1 and 4, and shift others to the right
        column1_name = column_names[0]
        column4_name = column_names[3]
        other_columns = ", ".join(column_names[1:3] + column_names[4:])
        
        # Create a new table with the modified column order and preserve data from column 1
        create_table_sql = f"CREATE TABLE {table_name}_new AS SELECT {column4_name}, {other_columns}, {column1_name} AS temp_column FROM {table_name};"
        
        cursor.execute(create_table_sql)
        
        # Drop the old table
        cursor.execute(f"DROP TABLE {table_name};")
        
        # Rename the new table to the original table name
        cursor.execute(f"ALTER TABLE {table_name}_new RENAME TO {table_name};")

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Column positions swapped successfully.")

def create_plots_directory():
    # Get the current directory of the script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Create the 'plots' directory if it doesn't exist
    plots_directory = os.path.join(script_directory, 'plots')
    if not os.path.exists(plots_directory):
        os.mkdir(plots_directory)
        print("Directory 'plots' created successfully.")
    else:
        print("Directory 'plots' already exists.")

if __name__ == "__main__":
    create_plots_directory()