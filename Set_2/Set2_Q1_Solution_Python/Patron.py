import Book

class Patron:
    
    def __init__(self, name : str, patron_id : str, books_checked_out : list) -> None:
        self._name = name
        self._patron_id = patron_id
        self._books_checked_out = books_checked_out
    
    def checkout_book(self, book : Book) -> None:
        if book in self._books_checked_out:
            print("This book", book._title, "is already issued to",self._name,"ID",self._patron_id)
            return
        self._books_checked_out.append(book)
        book._available_copies-=1
    
    def return_book(self, book : Book) -> None:
        if not book in self._books_checked_out:
            print("This book", book._title, "is not issued to",self._name,"ID",self._patron_id)
            return
        self._books_checked_out.remove(book)
        book._available_copies+=1
    
    def __str__(self) -> str:
        info = ''
        info+="Patron Info\n"
        info+="Name: " + self._name + "\n"
        info+="Patron ID: " + self._patron_id + "\n"
        
        book_titles = ''
        for book in self._books_checked_out:
            book_titles+=book._title+"\n"
        
        info+="Books Checkedout\n"
        info+=book_titles[:-1]
        return info
    
    def display_info(self):
        print(self)
        
        
    