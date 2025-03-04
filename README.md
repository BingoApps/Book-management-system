# Book-management-system
This is a simple Command Line Interface (CLI) application written in Python for managing a book store's inventory. It allows users to add, view, remove, and search for books.
## Features

* **Add Books:** Add new books with details like title, author, ISBN, genre, price, and quantity.
* **Prevent Duplicates:** Ensures that books with the same ISBN are not added multiple times.
* **View Books:** Display all books in a formatted table.
* **Remove Books:** Delete books by their ISBN.
* **Search Books:** Search books by title or author.
* **Data Persistence:** Book data is stored in a JSON file (`my_books.json`) and loaded on startup.
* **Error Handling:** Provides basic error messages for invalid inputs.

* How to Run

1.  **Prerequisites:**
    * Python 3.x installed on your system.

2.  **Download the Project:**
    * Download the project files (either by cloning the GitHub repository or downloading the ZIP file).

3.  **Navigate to the Project Directory:**
    * Open a terminal or command prompt and navigate to the directory where you saved the project files.

4.  **Run the Application:**
    * Execute the following command:
        ```bash
        assignment.py
        ```
5. **Use the Menu:**
    * The application will display a menu with options to add, view, remove, and search for books.
    * Enter the number corresponding to your desired action.
    * Follow the prompts.
  
   ## Project Structure

* `assignment.py`: The main entry point of the application.
* `book_store.py`: Handles loading and saving book data to the JSON file.
* `add_books.py`: Contains the function to add new books.
* `veiw_books.py`: Contains the function to display all books.
* `delete_books.py`: Contains the function to remove books.
* `search_books.py`: contains the function to search books.
* `my_books.json`: Stores the book data in JSON format.
