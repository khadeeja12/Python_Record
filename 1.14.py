import os

# Function to create a directory
def create_directory(directory_name):
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to list contents of a directory
def list_directory(directory_path):
    try:
        files = os.listdir(directory_path)
        print(f"Contents of '{directory_path}':")
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Directory '{directory_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to search for '.py' files in a directory
def search_py_files(directory_path):
    try:
        print(f"Searching for .py files in '{directory_path}':")
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.py'):
                    print(os.path.join(root, file))
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to remove a particular file
def remove_file(file_path):
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"File '{file_path}' removed successfully.")
        else:
            print(f"File '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Menu-driven program
def main():
    while True:
        print("\n--- OS Module Operations ---")
        print("1. Create a directory")
        print("2. Directory listing")
        print("3. Search for '.py' files")
        print("4. Remove a particular file")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            directory_name = input("Enter the directory name to create: ")
            create_directory(directory_name)

        elif choice == '2':
            directory_path = input("Enter the directory path to list: ")
            list_directory(directory_path)

        elif choice == '3':
            directory_path = input("Enter the directory path to search for '.py' files: ")
            search_py_files(directory_path)

        elif choice == '4':
            file_path = input("Enter the file path to remove: ")
            remove_file(file_path)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

# Call the main function
if __name__ == "__main__":
    main()
