def add_a_book(book_list):
    try:
        title = input("Book name / Title? ")
        author = input("Who wrote it / Author? ")
        isbn = input("Book number / Serial ? ")
        genre = input("What kind of book / Genre? ")
        price = float(input("How much / price? "))
        quantity = int(input("Total quantity? "))

        if not title or not author or not isbn or not genre:
            print("You need to fill in everything!")
            return

        if price <= 0:
            print("Price has to be more than zero!")
            return

        if quantity < 0:
            print("Can't have less than zero books!")
            return

        for book in book_list:
            if book["isbn"] == isbn:
                print("We already have that book!")
                return

        new_book = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "genre": genre,
            "price": price,
            "quantity": quantity
        }
        book_list.append(new_book)
        print("Book added!")

    except ValueError:
        print("Something went wrong with the numbers.")
