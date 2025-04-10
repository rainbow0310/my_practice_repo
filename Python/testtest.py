class Book:
    def __init__(self, title, author, genre, is_checked_out=False):
        self.title = title   
        self.author = author
        self.genre = genre
        self.is_checked_out = is_checked_out      

    def __str__(self):
        return f"title by author {self.genre}  : {self.is_checked_out}"
    
    def check_out(self):
        if self.is_checked_out == True:
            print ("This book is already checked out.")
        else:
            self.is_checked_out = True
    
    def return_book(self):
        if self.is_checked_out == False:
             print ("This book is already checked out.")
        else:
            self.is_checked_out = True
    
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author
    
    def get_genre(self):
        return self.genre
    
    def is_checked_out_method (self):
        return self.is_checked_out

"""
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
book1.get_author()
book1.get_genre()
book1.is_checked_out_method() COME BACK

book1.check_out()

book1.is_checked_out()
print(book1)

book1.return_book()
print(book1)
"""
