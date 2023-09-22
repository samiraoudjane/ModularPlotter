import os

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

file_path_3 = "processing.db"

if os.path.exists(file_path_3):
    os.remove(file_path_3)
    print(f"{file_path_3} has been deleted.")
else:
    print(f"{file_path_3} not found. No action taken.")
