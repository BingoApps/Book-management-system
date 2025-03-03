
def delete_a_book(book_list):
    isbn_to_remove = input("Which book to delete (ISBN)? ")
    for i, book in enumerate(book_list):
        if book["isbn"] == isbn_to_remove:
            del book_list[i]
            print("Book deleted!")
            return
    print("Didn't find that book.")