# Reading the file

def read_file(file_name):
    # Try-Except for error handling 
    try:
        # Open file in read mode
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
    # File not found error
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
    # Any other error
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

read_file('./Week3/File Handling/data.txt')

# Writing to the file

def write_to_file(user_input):
    try:
        # Write user input to output.txt
        with open('./Week3/File Handling/output.txt', 'w') as file:
            file.write(user_input)
        print("Data written successfully.")
    # Input/Output error
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")
    # Any other error
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

user_text = input("Enter some text to write to output.txt: ")
write_to_file(user_text)

# Counting Words

def read_and_count_words(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            print(f"The file contains {word_count} words.")
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

read_and_count_words('data.txt')
