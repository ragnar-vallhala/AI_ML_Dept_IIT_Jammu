import Library, Patron, Book



def main():
    book1 = Book.Book("Famous Book",            "Great Writer",     "shjg5f532vsd",     5, 8)
    book2 = Book.Book("Not so famous Book",     "Famous Writer",    "shjg5f532vsd",     12, 45)
    book3 = Book.Book("Eating Habits",          "Foody Writer",     "shjg5f532vsd",     14, 14)
    book4 = Book.Book("Sleeping Strategy",      "Lazy Writer",      "shjg5f532vsd",     14, 73)
    book5 = Book.Book("Get Marks in One day",   "Naughty Writer",   "shjg5f532vsd",     8, 12)
    book6 = Book.Book("Last Book",              "Dead Writer",      "shjg5f532vsd",     0, 1)
    books = [book1, book2, book3, book4, book5, book6]
    
    
    patron1 = Patron.Patron("Famour Reader",    "v654bj3r267t", [])
    patron2 = Patron.Patron("Lazy Reader",      "vhs5bj3r267t", [book1])
    patron3 = Patron.Patron("Crazy Reader",     "vhr8rj3r267t", [book2, book3])
    patron4 = Patron.Patron("Swaggy Reader",    "vh546j3r267t", [])
    patrons = [patron1,patron2,patron3,patron4]
    
    
    library = Library.Library()
    library.add_book(book1)
    library.add_book(book3)
    library.add_book(book5)
    library.add_book(book5)
    library.add_book(book2)
    
    library.register_patron(patron1)
    library.register_patron(patron2)
    library.register_patron(patron3)
    library.register_patron(patron4)
    library.register_patron(patron1)
    
    patron4.checkout_book(book1)
    library.remove_book(book6)
    library.display_books()
    
    
if __name__ == '__main__':
    print("Starting........")
    main()