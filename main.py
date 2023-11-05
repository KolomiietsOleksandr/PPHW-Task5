from encryptions import encrypt
from encryptions import decrypt

def read_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None

def write_to_file(file_name, data):
    try:
        with open(file_name, 'w') as file:
            file.write(data)
        print(f"Result saved to '{file_name}'.")
    except Exception as e:
        print(f"Error: {e}")
