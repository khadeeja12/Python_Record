# Function to check if one string is a substring of another
def check_substring(main_string, sub_string):
    if sub_string in main_string:
        print(f"'{sub_string}' is a substring of '{main_string}'")
    else:
        print(f"'{sub_string}' is not a substring of '{main_string}'")

# Function to count occurrences of a character in a string
def count_occurrences(string, char):
    count = string.count(char)
    print(f"The character '{char}' appears {count} times in the string.")

# Function to replace a substring with another substring
def replace_substring(string, old_substring, new_substring):
    new_string = string.replace(old_substring, new_substring)
    print(f"After replacing '{old_substring}' with '{new_substring}', the new string is: {new_string}")

# Function to convert the string to uppercase
def convert_to_upper(string):
    upper_string = string.upper()
    print(f"The string in uppercase is: {upper_string}")

# Main program
def main():
    while True:
        print("\nMenu:")
        print("1. Check if a String is a Substring of Another String")
        print("2. Count Occurrences of a Character")
        print("3. Replace a Substring with Another Substring")
        print("4. Convert String to Uppercase")
        print("5. Exit")

        # Take user choice
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            main_string = input("Enter the main string: ")
            sub_string = input("Enter the substring to check: ")
            check_substring(main_string, sub_string)

        elif choice == '2':
            string = input("Enter the string: ")
            char = input("Enter the character to count: ")
            count_occurrences(string, char)

        elif choice == '3':
            string = input("Enter the string: ")
            old_substring = input("Enter the substring to replace: ")
            new_substring = input("Enter the new substring: ")
            replace_substring(string, old_substring, new_substring)

        elif choice == '4':
            string = input("Enter the string: ")
            convert_to_upper(string)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

# Run the main program
main()
