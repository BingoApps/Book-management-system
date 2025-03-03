def search_books(book_list):
    search_term = input("Enter title or author to search: ").lower()
    found_books = []

    for book in book_list:
        if search_term in book["title"].lower() or search_term in book["author"].lower():
            found_books.append(book)

    if found_books:
        print("Found books:")
        print("Title   Author   ISBN   Genre   Price   Quantity")
        print("-------------------------------------------------")
        for book in found_books:
            print(book["title"], "   ", book["author"], "   ", book["isbn"], "   ", book["genre"], "   ", book["price"], "   ", book["quantity"])
    else:
        print("No books found matching your search.")