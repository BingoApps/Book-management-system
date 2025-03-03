def show_all_books(book_list):
    if not book_list:
        print("No books to show!")
        return

    print("Title   Author   ISBN   Genre   Price   Quantity")
    print("-------------------------------------------------")

    for book in book_list:
        print(book["title"], "   ", book["author"], "   ", book["isbn"], "   ", book["genre"], "   ", book["price"], "   ", book["quantity"])