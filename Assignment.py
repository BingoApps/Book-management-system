import book_store
import add_books
import veiw_books
import delete_books
import search_books

def do_stuff():
    book_list = book_store.get_books()

    while True:
        print(" Welcome to Laurine's Book Store Management System")
        print("1. Add a book")
        print("2. View Books")
        print("3. Search books")
        print("4. Remove Books")
        print("5. Exit")

        choice = input("Please enter what you want to do? ")

        if choice == "1":
            add_books.add_a_book(book_list)
            book_store.save_the_books(book_list)
        elif choice == "2":
            veiw_books.show_all_books(book_list)
        elif choice == "3":
            search_books.search_books(book_list)
        elif choice == "4":
            delete_books.delete_a_book(book_list)
            book_store.save_the_books(book_list)
        elif choice == "5":
            print("Okay, bye!")
            break
        else:
            print("Huh? Didn't get that.")

if __name__ == "__main__":
    do_stuff()



