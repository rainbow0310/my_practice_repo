from book import Book
books = []
with open("books.txt") as file:
    for line in file:
            book_info = line.strip().split(",")  #removes the new line and then split it
            one_book = Book(book_info[0], book_info[1], book_info[2])
            books.append(one_book)
    print(books)

book1 = books[0]
book2 = books[1]
book3 = books[2]
book4 = books[3]
book5 = books[4]

book1.get_title()
print(book1.get_title())
book1.get_author()
print(book1.get_author())
book1.get_genre()
print(book1.get_genre())
book1.is_checked_out_method() 
print(book1.is_checked_out_method())

book1.check_out()

book1.is_checked_out_method()
print(book1)

book1.return_book()
print(book1)
