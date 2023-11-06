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

def process(user_input):
    if user_input == "1":
        data = input("Enter the data for encryption/decryption: ")
    elif user_input == "2":
        file_name = input("Enter file name: ")
        data = read_from_file(file_name)
        if data is None:
            return
    else:
        print("False choice")
        return

    key = input("Enter key: ")

    operation = input("Select the operation (encrypt - 'e' or decrypt - 'd'): ")

    if operation == 'e':
        result = encrypt(data, key)
    elif operation == 'd':
        result = decrypt(data, key)
    else:
        print("False operation")
        return

    output_file_name = input("Enter a file name to save the result (or press Enter to not save to a file): ")
    if output_file_name:
        write_to_file(output_file_name, result)
    else:
        print("Result:", result)

def main():
    while(True):
        user_input = input("From console (1) or file (2): ")
        process(user_input)

if __name__ == "__main__":
    main()
