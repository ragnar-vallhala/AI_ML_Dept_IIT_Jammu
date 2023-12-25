import Book
import Patron

class Library:
    _books = {}
    _patrons = []
    
    def __init__(self) -> None:
        pass
    
    def add_book(self, book : Book):
        if book in Library._books:
            Library._books[book]+=1
            return
        Library._books[book] = 1
    
    def remove_book(self, book : Book):
        if not book in Library._books:
            print(book._title, "is not in the library to remove.")
            return
        Library._books[book] -= 1
        if Library._books[book]<= 0:
            del Library._books[book]
        
    def register_patron(self, patron: Patron):
        if patron in Library._patrons:
            print(patron._name, "is already a patron.")
            return
        Library._patrons.append(patron)    
    
    def remove_patron(self, patron : Patron):
        if not patron in Library._patrons:
            print(patron._name, "is not patron.")
            return
        Library._patrons.remove(patron)
    
    def display_books(self):
        print("Following are the books present in the Library")
        for book in Library._books.keys():
            print(book._title,"Count: ",Library._books[book])
            book.display_info()       
        print("End")
    
    def display_patrons(self):
        print("Following are the patrons of the Library")
        for patron in Library._patrons:
            patron.display_info()       
        print("End")
    
    
    