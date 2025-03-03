import json
import os # for files

FILE_NAME = "my_books.json" # where the books live

def get_books():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as f:
                return json.load(f) # get the books from the file
        except json.JSONDecodeError:
            print("File is messed up. Starting with no books.")
            return []
    else:
        print("No file found. Starting with no books.")
        return []

def save_the_books(book_list):
    with open(FILE_NAME, "w") as f:
        json.dump(book_list, f, indent=4)

